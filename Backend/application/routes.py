from flask import render_template, url_for, flash, redirect
from application import app
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post

posts = [
    {
        'author': 'TC',
        'title': 'header ',
        'content': 'First post content',
        'date_posted': 'October 27, 2022'
    },
    {
        'author': 'Alan',
        'title': 'header',
        'content': 'Second post content',
        'date_posted': 'October 28, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'tc@test.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

