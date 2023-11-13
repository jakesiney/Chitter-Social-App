from example_routes import apply_example_routes
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.peep_repository import PeepRepository
from lib.user_repository import UserRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# a router for a login page


@app.route('/login', methods=['GET'])
def login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.getuser()
    return render_template("login.html", user=user)


@app.route('/', methods=['GET'])
def all_peeps():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.all()
    return render_template("peeps/index.html", peeps=peeps)

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji


# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
