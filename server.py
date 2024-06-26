import os
from flask import Flask, render_template, make_response, jsonify, redirect
from flask_login import LoginManager, logout_user, login_required, login_user
from data import db_session
from data.users import User
from forms.loginform import LoginForm
from forms.registerform import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if True:#user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    # if form.validate_on_submit():
    #     if form.password.data != form.password_again.data:
    #         return render_template('register.html', title='Регистрация',
    #                                form=form,
    #                                message="Пароли не совпадают")
    #     db_sess = db_session.create_session()
    #     if db_sess.query(User).filter(User.email == form.email.data).first():
    #         return render_template('register.html', title='Регистрация',
    #                                form=form,
    #                                message="Такой пользователь уже есть")
    #     user = User(
    #         name=form.name.data,
    #         email=form.email.data,
    #         about=form.about.data
    #     )
    #     user.set_password(form.password.data)
    #     db_sess.add(user)
    #     db_sess.commit()
    #     return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify({'error': 'not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    db_session.global_init("database.db")
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
