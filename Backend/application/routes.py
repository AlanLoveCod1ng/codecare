import datetime
import uuid
from flask import redirect, request, jsonify, make_response
from application import app, session, db_engine, Base
from application.models import Account, Patient, Provider, Patient, Provider, Record, Notification, Notification_Provider, State, Infe_city, Env_city
from functools import wraps
from sqlalchemy import func
import jwt

from sqlalchemy import Column, Integer, String


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return make_response('Token is missing!')
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],"HS256")
        except:
            return make_response('Token is invalid', 403)
        account = session.query(Account).filter(Account.account_id == data['account_id']).first()
        return f(account, *args, **kwargs)
    return decorated

@app.route("/<name>/<address>")
@app.route("/home")
def home(name, address):
    print(name)
    print(address)
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
    try:
        email = form['email']
        password = form['password']
    except:
        return make_response('Error with form!', 401)
        
    account = session.query(Account).filter(Account.email == email).first()

    if account and password == account.password:
        token = jwt.encode({'account_id': account.account_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')
        return redirect('/account?token='+token)
    else:
        return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})

@app.route("/register", methods=['GET', 'POST'])
def register():
    data = request.form
    try:
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone = data['phone']
        password = data['password']
    except:
        return make_response("Error with form.", 401)

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
    return_list = []
    filter = request.args.get("filter", "")
    first_number = request.args.get("first", None)
    if account.is_patient == 1:
        return jsonify({'message' : 'Provider Only.'})
    elif account.is_patient != 1:
        provider_id = account.id
        notifications = session.query(
            Notification, Notification_Provider
        ).filter(
            Notification.n_id == Notification_Provider.n_id
        ).filter(
            Notification_Provider.provider_id == provider_id
        )
        if filter == "waiting":
            notifications = notifications.filter(Notification_Provider.condition == 1)
        elif filter == "processed":
            notifications = notifications.filter(Notification_Provider.condition == 0)
        if first_number and first_number.isnumeric():
            notifications = notifications[:int(first_number)]
        for n, np in notifications:
            noti_dict = {}
            city_id = n.city_id
            city = session.query(Infe_city).filter(Infe_city.city_id == city_id)
            if city.count() == 0:
                city = session.query(Env_city).filter(Env_city.city_id == city_id)
            city = city.first()
            city_name = city.city_name
            state_name = session.query(State).filter(State.state_id == city.state_id).first().state_name
            content = n.content
            dt = n.datetime
            todo = np.condition
            noti_dict["account_id"] = account.account_id
            noti_dict["city"] = city_name
            noti_dict["state"] = state_name
            noti_dict["content"] = content
            noti_dict['datetime'] = dt
            noti_dict['waiting to be processed'] = todo
            return_list.append(noti_dict)
    return jsonify(return_list)
    
# return the location record of certain patient
@app.route("/record", methods = ['GET'])
@token_required
def location_record(account):
    if account.is_patient != 1:
        return make_response("Patient Only.", 403)
    first_number = request.args.get("first", None)
    patient_id = account.id
    return_dict = {}
    try:
        records = session.query(Record).filter(Record.patient_id == patient_id)
    except:
        return make_response("Can't fetch data.", 401)
    if first_number and first_number.isnumeric():
        records = records[:int(first_number)]
    for record in records:
        record_dict = {}
        for key in record.__dict__:
            if key != '_sa_instance_state':
                record_dict[key] = record.__dict__[key]
        return_dict[record.location_id] = record_dict
    
    return jsonify(return_dict)