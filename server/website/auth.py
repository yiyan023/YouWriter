from flask import Blueprint, render_template, request, flash, redirect, url_for
import pymongo
import certifi

from . import user

auth = Blueprint('auth', __name__)


# @auth.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('login.html')


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')

        existing_user = user.find_one({'username': username})
        existing_password = user.find_one({'password': password1})

        if existing_user and existing_password and existing_user['username'] == username and existing_password['password'] == password1:
            return redirect("http://localhost:3000")
        else:
            flash("Incorrect login information. Try again.")

    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('login.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        existing_user = user.find_one({'username': username})
        existing_email = user.find_one({'email': email})

        if len(email) < 4:
            # flash shows a message on the screen
            flash('Email must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        elif existing_user and username == existing_user['username']:
            flash('That username already exists. Please choose another one')
        elif existing_email and email == existing_email['email']:
            flash('That email is already registered. Please enter another one.')
        else:
            user_input = {'firstname': firstName, 'username': username,
                          'email': email, 'password': password1}
            user.insert_one(user_input)

            user_data = user.find_one({"email": email})
            new_email = user_data["email"]

            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template('signup.html')
