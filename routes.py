from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db, bcrypt
from app.models import Train, Station, Vendor, User
from app.forms import RegistrationForm, LoginForm, SearchForm
from flask_login import login_user, current_user, logout_user, login_required
import json

main = Blueprint('main', __name__)
users = Blueprint('users', __name__)

@main.route("/")
@main.route("/home")
def home():
    form = SearchForm()
    return render_template('index.html', form=form)

@main.route("/station/<int:station_id>")
def station(station_id):
    station = Station.query.get_or_404(station_id)
    vendors = Vendor.query.filter_by(station_id=station_id).all()
    for vendor in vendors:
        vendor.menu = json.loads(vendor.menu)
    return render_template('station.html', station=station, vendors=vendors)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))