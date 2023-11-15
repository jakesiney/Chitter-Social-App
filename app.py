import os
from flask import Flask, request, render_template, redirect, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from lib.database_connection import get_flask_database_connection
from lib.peep_repository import PeepRepository
from lib.user_repository import UserRepository
from lib.user import User
from lib.peep import Peep
import dotenv
from datetime import datetime


login_manager = LoginManager()
dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    return repository.get_by_id(int(user_id))


@app.route('/', methods=['GET'])
def get_login():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user_name = request.form['user_name']
    password = request.form['password']
    valid = repository.validate_login(user_name, password)
    if valid:
        user = repository.get_by_username(user_name)
        login_user(user)
        session['user_name'] = user_name
        flash('Logged in successfully, welcome to Chitter')
        return redirect('/home')
    else:
        raise Exception("Invalid login, try again")


@app.route('/newpost', methods=['GET'])
@login_required
def new_post():
    return render_template('peep.html')


@app.route('/createpost', methods=['POST'])
@login_required
def create_post():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peep = request.form['peep']
    posted_on = datetime.now()
    user_id = current_user.id
    user_name = current_user.user_name
    post = Peep(None, posted_on, peep, user_name, user_id)
    repository.create_new_peep(post)
    return redirect('/home')


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@app.route('/createuser', methods=['POST'])
def create_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user_name = request.form['user_name']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    user = User(None, user_name, first_name, last_name, email, password)
    repository.create_user(user)
    login_user(user)
    return redirect('/home')


@app.route('/home', methods=['GET'])
def all_peeps():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.all()
    return render_template("home.html", peeps=peeps)


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
