from flask import redirect, request, jsonify, make_response
from application import app, session, db_engine, Base
from application.models import Account, Patient, Provider, Patient, Jurisdiction, Record, Notification, Notification_Provider, Notification_Patient, State, City
from functools import wraps
from sqlalchemy import func
import datetime
import requests, json, jwt, random

from sqlalchemy import Column, Integer, String, desc


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


@app.route('/account')
@token_required
def account(account):
    return_dict = {}
    for key in account.__dict__:
        if key != '_sa_instance_state':
            return_dict[key] = account.__dict__[key]
    return_dict['token'] = request.args.get('token')
    return jsonify(return_dict)
    

@app.route("/login", methods=['GET'])
def login():
    print('called')
    try:
        email = request.args['email']
        password = request.args['password']
    except:
        return make_response('Error with args!', 401)
        
    account = session.query(Account).filter(Account.email == email).first()

    if account and password == account.password:
        token = jwt.encode({'account_id': account.account_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')
        return redirect('/account?token='+token)
    else:
        return make_response('Could not verify!', 401)

@app.route("/register", methods=['GET'])
def register():
    data = request.args
    try:
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone = data['phone']
        password = data['password']
        state = data['state'].capitalize()
    except:
        return make_response("Error with form.", 401)

    user = session.query(Account).filter(Account.email == email).first()

    if not user:
        # database ORM object
        try:
            id = session.query(func.max(Account.id)).first()[0]
            potential_provider = session.query(Jurisdiction, State).filter(State.state_name == state).filter(Jurisdiction.state_id == State.state_id).all()
            chosen_provider = random.choice(potential_provider)[0].provider_id
            newUser = Patient(patient_id = id+1, provider_id = chosen_provider)
            newAccount = Account(id = id+1, email = email, phone = phone, is_patient = 1, password = password, first_name = first_name, last_name = last_name)
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
        provider_id = account.id
        notifications = session.query(
            Notification, Notification_Patient
        ).filter(
            Notification.n_id == Notification_Provider.n_id
        ).filter(
            Notification_Provider.provider_id == provider_id
        ).order_by(desc(Notification.datetime))
        if filter == "waiting":
            notifications = notifications.filter(Notification_Provider.processed == 0)
        elif filter == "processed":
            notifications = notifications.filter(Notification_Provider.processed == 1)
        if first_number and first_number.isnumeric():
            notifications = notifications[:int(first_number)]
        for n, np in notifications:
            noti_dict = {}
            city_id = n.city_id
            city = session.query(City).filter(City.city_id == city_id)
            city = city.first()
            city_name = city.city_name
            state_name = session.query(State).filter(State.state_id == city.state_id).first().state_name
            content = n.content
            dt = n.datetime
            todo = np.processed
            noti_dict["account_id"] = account.account_id
            noti_dict["city"] = city_name
            noti_dict["state"] = state_name
            noti_dict["content"] = content
            noti_dict['datetime'] = dt
            noti_dict['processed'] = todo
            return_list.append(noti_dict)
    elif account.is_patient != 1:
        provider_id = account.id
        notifications = session.query(
            Notification, Notification_Provider
        ).filter(
            Notification.n_id == Notification_Provider.n_id
        ).filter(
            Notification_Provider.provider_id == provider_id
        ).order_by(desc(Notification.datetime))
        if filter == "waiting":
            notifications = notifications.filter(Notification_Provider.processed == 0)
        elif filter == "processed":
            notifications = notifications.filter(Notification_Provider.processed == 1)
        if first_number and first_number.isnumeric():
            notifications = notifications[:int(first_number)]
        for n, np in notifications:
            noti_dict = {}
            city_id = n.city_id
            city = session.query(City).filter(City.city_id == city_id)
            city = city.first()
            city_name = city.city_name
            state_name = session.query(State).filter(State.state_id == city.state_id).first().state_name
            content = n.content
            dt = n.datetime
            todo = np.processed
            noti_dict['notification_id'] = n.n_id
            noti_dict["account_id"] = account.account_id
            noti_dict["city"] = city_name
            noti_dict["state"] = state_name
            noti_dict["content"] = content
            noti_dict['datetime'] = dt
            noti_dict['processed'] = todo
            return_list.append(noti_dict)
    return jsonify(return_list)
    
    
@app.route("/provider", methods = ['GET'])
@token_required
def get_provider(account):
    if account.is_patient == 0:
        return make_response("Patient Only" ,401)
    patient_id = account.id
    provider_id = session.query(Patient).filter(Patient.patient_id == patient_id).first().provider_id
    provider = session.query(Account).filter(Account.id == provider_id).first()
    provider_dict = {}
    provider_dict['patient_id'] = provider.id
    provider_dict['email'] = provider.email
    provider_dict['phone'] = provider.phone
    provider_dict['first_name'] = provider.first_name
    provider_dict['last_name'] = provider.last_name
    return jsonify(provider_dict)    
    
@app.route("/patients", methods = ['GET'])
@token_required
def get_patients(account):
    if account.is_patient == 1:
        return make_response("Provider Only" ,401)
    provider_id = account.id
    patients = session.query(Patient, Account).filter(Patient.patient_id == Account.id).filter(Patient.provider_id == provider_id)
    return_list = []
    for patient, account in patients:
        patient_dict = {}
        patient_dict['patient_id'] = account.id
        patient_dict['email'] = account.email
        patient_dict['phone'] = account.phone
        patient_dict['first_name'] = account.first_name
        patient_dict['last_name'] = account.last_name
        return_list.append(patient_dict)
    return jsonify(return_list)

# return the location record of certain patient
@app.route("/record/<patient_id>", methods = ['GET'])
@token_required
def location_record(account,patient_id):
    first_number = request.args.get("first", None)
    return_list = []
    try:
        records = session.query(Record).filter(Record.patient_id == patient_id).order_by(desc(Record.datetime))
    except:
        return make_response("Invalid Patient ID.", 401)
    if first_number and first_number.isnumeric():
        records = records[:int(first_number)]
    for record in records:
        record_dict = {}
        for key in record.__dict__:
            if key != '_sa_instance_state':
                record_dict[key] = record.__dict__[key]
        return_list.append(record_dict)
    
    return jsonify(return_list)

# return the location record of certain patient
@app.route("/send/<notification_id>", methods = ['GET','POST'])
@token_required
def send_notification(account,notification_id):
    if account.is_patient != 0:
        return make_response("Provider Only.", 403)
    provider_id = account.id
    sent_notification = session.query(Notification_Provider).filter(Notification_Provider.n_id == notification_id).filter(Notification_Provider.provider_id == provider_id)
    if len(sent_notification.all()) == 0:
        return make_response("Invalid ID.", 403)
    notification = sent_notification.first()
    to_add = []
    if notification.processed == 1:
        return make_response("Notification Already processed.", 201)
    target_patients = session.query(Patient).filter(Patient.provider_id == provider_id)
    for patient in target_patients:
        np = Notification_Patient(n_id = notification_id, patient_id = patient.patient_id, read = 0)
        to_add.append(np)
    for n in sent_notification:
        n.processed = 1
    try:
        session.add_all(to_add)
        session.commit()
    except:
        return make_response("Error with inserting record.", 401)
    return make_response("Notification sent to %d patient"%(len(target_patients.all())), 201)

# return the location record of certain patient
@app.route("/deny/<notification_id>", methods = ['GET','POST'])
@token_required
def deny_notification(account,notification_id):
    if account.is_patient != 0:
        return make_response("Provider Only.", 403)
    provider_id = account.id
    sent_notification = session.query(Notification_Provider).filter(Notification_Provider.n_id == notification_id).filter(Notification_Provider.provider_id == provider_id)
    if len(sent_notification.all()) == 0:
        return make_response("Invalid ID.", 403)
    notification = sent_notification.first()
    if notification.processed == 1:
        return make_response("Notification Already processed.", 201)
    for n in sent_notification:
        n.processed = 1
    try:
        session.commit()
    except:
        return make_response("Error with inserting record.", 401)
    return make_response("Notification denied.", 201)

@app.route("/read/<notification_id>", methods = ['GET','POST'])
@token_required
def readNotification(account,notification_id):
    if account.is_patient == 0:
        return make_response("Patient Only.", 403)
    patient_id = account.id
    read_notification = session.query(Notification_Patient).filter(Notification_Patient.n_id == notification_id).filter(Notification_Patient.patient_id == patient_id)
    if len(read_notification.all()) == 0:
        return make_response("Invalid ID.", 403)
    notification = read_notification.first()
    if notification.read == 1:
        return make_response("Notification Already processed.", 201)
    for n in read_notification:
        n.read = 1
    try:
        session.commit()
    except:
        return make_response("Error with inserting record.", 401)
    return make_response("Notification read.", 201)

@app.route("/new_record", methods = ['GET','POST'])
@token_required
def add_record(account):
    if account.is_patient != 1:
        return make_response("Patient Only.", 403)
    try:
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        dt = request.args.get('datetime')
    except:
        return make_response("Missing Args", 403)
    try:
        datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    except:
        return make_response("Invalid datetime format.", 401)
    patient_id = account.id
    response = requests.get("https://api.3geonames.org/%f,%f.json"%(lat,lon)).text
    data = json.loads(response)
    city_name = data['nearest']['city']
    state_name = data['nearest']['prov']
    try:
        state_id = session.query(State).filter(State.state_name == state_name).first().state_id
    except:
        return make_response("Not in US.", 401)
    new_record = Record(patient_id = patient_id, latitude = lat, longitude = lon, city = city_name, state_id = state_id, datetime = dt)
    try:
        session.add(new_record)
        session.commit()
    except:
        return make_response("Error inserting data.", 403)
    return make_response("Successfully add record", 202)




# create a new notification based on the fake service
# @app.route("/add_notification", methods = ['GET','POST'])
# def add_notification():

    
#     response_API = requests.get('http://192.168.0.143:8000/api/disease')
#     data = response_API.text
#     parse_json = json.loads(data)

#     for i in range(len(parse_json)):
#         cityName = parse_json[i]['state']
#         newContent = parse_json[i]['name']
#         timeStamp = parse_json[i]['timestamp']
#         # query the city database to find the corresponding cityID
#         try:
#             city_resp = session.query(City).filter(City.city_name == cityName).first()
#             print(city_resp)
#         except:
#             return make_response("No result found", 401) 
#         # city_resp = city_resp.first()
#         cityId = city_resp.city_id
#         new_notification = Notification(city_id = cityId, content = newContent, datetime = timeStamp, notified = 0)
        
#         try:
#             session.add(new_notification)
#             session.commit()
#         except:
#             return make_response("Error inserting data.", 403) 
#     return make_response("Successfully add new notifications", 202)

# @app.route("/add_notification", methods = ['GET','POST'])
def add_notification_helper():
    response_API = requests.get('http://192.168.0.143:8000/api/disease')
    data = response_API.text
    parse_json = json.loads(data)
    ret_list = []
    for i in range(len(parse_json)):
        cityName = parse_json[i]['city']
        newContent = parse_json[i]['name']
        timeStamp = parse_json[i]['timestamp']
        # query the city database to find the corresponding cityID
        try:
            city_resp = session.query(City).filter(City.city_name == cityName).first()
            print(city_resp)
        except:
            return make_response("No result found", 401) 
        # city_resp = city_resp.first()
        cityId = city_resp.city_id
        new_notification = Notification(city_id = cityId, content = newContent, datetime = timeStamp, notified = 0)
        
        try:
            session.add(new_notification)
            session.commit()
        except:
            return make_response("Error inserting data.", 403) 
        
        # add notification into the return list
        noti_dict = {}
        noti_dict["city"] =  cityName
        noti_dict["content"] = newContent
        noti_dict["datetime"] = timeStamp
        ret_list.append(noti_dict)


        # binding notification with corresponding providers

        state_id = session.query(City).filter(City.city_name == cityName).first().state_id
        provider_id = session.query(Jurisdiction).filter(Jurisdiction.state_id == state_id).first().provider_id
        provider_group = session.query(Provider).filter(Provider.provider_id == provider_id)

        # for i in provider_group:
        #     print(i.provider_id)

        for provider in provider_group:
            np = Notification_Provider(n_id = new_notification.n_id, provider_id = provider.provider_id, processed = 0)

            try:
                session.add(np)
                session.commit()
            except:
                return make_response("Error with inserting", 401)

    return ret_list



@app.route("/add_notification", methods = ['GET','POST'])
# @token_required
def add_notification():
    # if account.is_patient != 0:
    #     return make_response("Provider Only", 403)
    
    noti_list = add_notification_helper()

    return jsonify(noti_list)



    

