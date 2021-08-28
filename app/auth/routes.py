from app.auth import authentication as at
from app.auth.forms import RegistrationForm, LoginForm
from flask import render_template, request, redirect, url_for, flash
from app.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user

@at.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged-in..!')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    # name = None
    # email = None
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = form.email.data

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash("User successfully registered")
        return redirect(url_for('authentication.login_the_user'))
    return render_template("registration.html", form=form)


# We need to tell the LoginManager about the login route (that its used for logging in)
# So in root package's (i.e. app) __init__ we took care of that
@at.route('/login', methods=['GET', 'POST'])
def login_the_user():
    if current_user.is_authenticated:
        flash('You are already logged-in..!')
        return redirect(url_for('main.display_books'))

    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(user_name=loginForm.name.data).first()
        if not user or not user.check_password(password=loginForm.password.data):
            flash("Invalid Credentials, please try again!")
            return redirect(url_for('authentication.login_the_user'))

        login_user(user, loginForm.stay_logged_in.data)  # login_user loads the User obj/id into the Session for remembrance
        return redirect(url_for('main.display_books'))

    return render_template("login.html", loginForm=loginForm)


@at.route('/logout')
@login_required
def logout_the_user():
    logout_user()
    return redirect(url_for('authentication.login_the_user'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
