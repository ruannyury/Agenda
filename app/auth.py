from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.tables import User
from app import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logado com sucesso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente!', category='error')
        else:
            flash('Não há cadastro.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/', methods=['GET', 'POST'])
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        username_db = User.query.filter_by(username=username).first()

        if user:
            flash('Email já existe', category='error')
        elif username_db:
            flash('Username já existe', category='error')
        elif len(email) < 4:
            flash('Email pequeno demais!', category='error')
        elif len(name) < 2:
            flash('Nome pequeno demais!', category='error')
        elif len(username) < 2:
            flash('Username pequeno demais!', category='error')
        elif len(password) < 7:
            flash('Senha precisa ter mais de 7 caracteres!', category='error')

        elif request.form.get('entrar'):
            return redirect(url_for('auth.login'))
        else:
            new_user = User(name=name,
                            email=email,
                            username=username,
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash('Conta criada!', category='sucess')
            return redirect(url_for('views.home'))

    return render_template('index.html', user=current_user)
