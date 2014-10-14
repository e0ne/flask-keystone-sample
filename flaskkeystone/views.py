from functools import wraps
from flask import Blueprint, render_template, request, redirect, session


import flask_keystoneauth

app = Blueprint('website', __name__, template_folder='templates')

from flask import current_app
keystone_auth = flask_keystoneauth.KeystoneAuth(current_app)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """

    return keystone_auth.authenticate(username, password)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = session.get('authorized', None)

        if not auth_token:  
            return redirect('login')
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/secret')
@requires_auth
def secret_page():
    return render_template('secret.html')


@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if check_auth(username, password):
            return redirect('/')
            # return render_template('login.html')
    return render_template('login.html')


@app.route("/logout")
def logout():
    keystone_auth.invalidate()

    request.authorization = None
    return redirect('/')
