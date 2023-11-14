import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.peep_repository import PeepRepository
from lib.user_repository import UserRepository


app = Flask(__name__)


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
        return redirect('/home')
    else:
        raise Exception("Invalid login, try again")


@app.route('/home', methods=['GET'])
def all_peeps():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.all()
    return render_template("home.html", peeps=peeps)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
