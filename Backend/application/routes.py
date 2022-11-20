import datetime
import uuid
from flask import redirect, request, jsonify, make_response
from application import app, session, db_engine, Base
from application.models import Account, Patient, Provider, Patient, Provider, Record
from functools import wraps
from sqlalchemy import func
import jwt

from sqlalchemy import Column, Integer, String


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return jsonify({'message' : 'Token is missing!'})
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],"HS256")
        except:
            return jsonify({'message' : 'Token is invalid'}), 403
        account = session.query(Account).filter(Account.account_id == data['account_id']).first()
        return f(account, *args, **kwargs)
    return decorated

@app.route("/")
@app.route("/home")
def home():
    return "good"


@app.route('/account')
@token_required
def account(account):
    return_dict = {}
    for key in account.__dict__:
        if key != '_sa_instance_state':
            return_dict[key] = account.__dict__[key]
    return_dict['token'] = request.args.get('token')
    return jsonify(return_dict)
    

@app.route("/login", methods=['POST'])
def login():
    form = request.form
    email = form['email']
    password = form['password']
    account = session.query(Account).filter(Account.email == email).first()

    if account and password == account.password:
        token = jwt.encode({'account_id': account.account_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')
        return redirect('/account?token='+token)
    else:
        return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})

@app.route("/register", methods=['GET', 'POST'])
def register():
    data = request.form
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone = data['phone']
    password = data['password']
    confirm_password = data.get('confirm_password')



    user = session.query(Account).filter(Account.email == email).first()

    if not user:
        # database ORM object
        try:
            id = session.query(func.max(Patient.patient_id)).first()[0]
            newUser = Patient(patient_id = id+1, provider_id = None)
            newAccount = Account(id = id, email = email, phone = phone, is_patient = 1, password = password, first_name = first_name, last_name = last_name)
            session.add(newAccount)
            session.add(newUser)
            session.commit()
        except:
            return make_response("Can't register.", 401)
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)
  
# return the all notifications which belong to 
@app.route("/notification",methods=['GET'])
@token_required
def read_notification(account):
    if account.is_patient == 1:
        return jsonify({'message' : 'Provider Only.'})
    
# return the location record of certain patient
@app.route("/record", methods = ['GET'])
@token_required
def location_record(account):
    if account.is_patient != 1:
        return jsonify({'message' : 'Patient Only.'})
    patient_id = account.id
    return_dict = {}
    records = session.query(Record).filter(Record.patient_id == patient_id)
    for record in records:
        record_dict = {}
        for key in record.__dict__:
            if key != '_sa_instance_state':
                record_dict[key] = record.__dict__[key]
        return_dict[record.location_id] = record_dict
    
    return jsonify(return_dict)