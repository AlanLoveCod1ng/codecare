import datetime
from flask import redirect, request, jsonify, make_response
from application import app, session
from application.models import Account
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
        return f(*args, **kwargs)
    return decorated
    
@app.route("/")
@app.route("/home")
def home():
    return "good"


@app.route('/overview')
@token_required
def overview():
    token = request.args.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'],'HS256')
    account_id = data['account_id']
    print(type(account_id))
    account = session.query(Account).filter(Account.account_id == account_id).first()
    return_dict = {}
    for key in account.__dict__:
        if key != '_sa_instance_state':
            return_dict[key] = account.__dict__[key]
    return_dict['token'] = token
    return jsonify(return_dict)
    


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = request.form
    email = form['email']
    password = form['password']
    account = session.query(Account).filter(Account.email == email).first()

    if account and password == account.password:
        token = jwt.encode({'account_id': account.account_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')
        return redirect('/overview?token='+token)
    else:
        return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})

