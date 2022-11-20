import datetime
from flask import redirect, request, jsonify, make_response
from application import app, session
from application.models import Account, Patient, Provider, Record
from functools import wraps
import jwt

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