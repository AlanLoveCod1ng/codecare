import datetime
from flask import render_template, url_for, flash, redirect, request, jsonify, make_response
from application import app, db, bcrypt
from application.models import Account, Post
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
    
# posts = [
#     {
#         'author': 'TC',
#         'title': 'header ',
#         'content': 'First post content',
#         'date_posted': 'October 27, 2022'
#     },
#     {
#         'author': 'Alan',
#         'title': 'header',
#         'content': 'Second post content',
#         'date_posted': 'October 28, 2022'
#     }
# ]

@app.route("/")
@app.route("/home")
def home():
    return "good"


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


# @app.route("/register", methods=['GET', 'POST'])
# def register():

#     return render_template('register.html', title='Register', form=form)

@app.route('/overview')
@token_required
def restrict():
    token = request.args.get('token')
    data = jwt.decode(token, app.config['SECRET_KEY'],'HS256')
    account_id = data['account_id']
    account = db.session.query(Account).filter(Account.account_id == account_id).first()
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
    account = db.session.query(Account).filter(Account.email == email).first()

    if account and password == account.password:
        token = jwt.encode({'account_id': account.account_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')
        return redirect('/overview?token='+token)
    else:
        return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})
# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))


# @app.route("/account")
# @login_required
# def account():
#     return render_template('account.html', title='Account')