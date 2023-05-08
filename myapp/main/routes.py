from flask import render_template, redirect, url_for, Blueprint
from flask_login import current_user
from myapp.main.forms import LoginForm
from myapp.models import User
from myapp import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
    return render_template('index/acc.html', title='Аккаунт')

@main.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('acc.html', title='Аккаунт')