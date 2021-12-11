import hashlib

from wtforms import Form, validators, \
    EmailField, PasswordField, StringField, IntegerField
import json
import flask
import userDB
import sqlite3
from flask_login import UserMixin

class UserRegisterForm(Form):
    email = EmailField('Email',
                       [validators.DataRequired(),
                        validators.Email()])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.length(min=8, max=30)])
    name = StringField('Username',
                       [validators.DataRequired(),
                        validators.length(min=3, max=30)])
    mobile_phone = StringField('Mobile',
                               [validators.DataRequired(),
                                validators.length(min=10, max=10)])
    zipcode = IntegerField('Zipcode', [validators.DataRequired()])


def register(raw_form):
    form = UserRegisterForm(raw_form)
    if not form.validate():
        return json.dumps({"Input error": form.errors}), 400

    hash_object = hashlib.sha256(str(form.password.data).encode('utf-8'))
    #print('Hashed Password', hash_object.hexdigest())
    user = (form.email.data, hash_object.hexdigest(),
            form.name.data, form.zipcode.data, form.mobile_phone.data)
    conn = None
    try:
        conn = sqlite3.connect("sqlite_db")
        cur = conn.cursor()
        sql = "INSERT INTO User" \
              "(email, password, name, zipcode, phone_number) " \
              "VALUES(?, ?, ?, ?, ?) "
        cur.execute(sql, user)
        conn.commit()
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
    return json.dumps({"error": ""}), 201


class UserLoginObj(UserMixin):
    def __init__(self, saved_user: userDB.User):
        self.username = saved_user.get_name()
        self.password_hash = saved_user.get_password()
        self.email = saved_user.get_email()
        self.user = saved_user

    def get_id(self):  # the primary key is email, so return email
        # get_id overwrite parent class method
        return self.email

    def get_email(self):
        return self.email

    @staticmethod
    def get(email):
        if not email:
            return None
        saved_user = userDB.select_user_by_email(email)
        print(saved_user)
        if not saved_user:
            return None
        return UserLoginObj(saved_user)


def set_user_cookie(email: str, resp):
    resp.set_cookie('user', email)


def need_login_response():
    return json.dumps({"error": "Please login first"}), 400


def user_login(email, password):
    try:
        print(email, password)
        if not email or not password:
            return json.dumps({"error": "invalid input"}), 400, None
        saved_user = userDB.select_user_by_email(email)
        print(saved_user)
        if not saved_user:
            return json.dumps({"error": f"No such email {email}"}), 400, None
        # To Do: md5
        if not password == saved_user.get_password():
            return json.dumps({"error": f"wrong password {email}"}), 400, None
        resp = flask.make_response(json.dumps({"error": ""}))
        # set_user_cookie(email, resp)
        return resp, 200, UserLoginObj(saved_user)
    except Exception as e:
        print(e)
        return json.dumps({"error": "Internal error"}), 500, None


def user_logout_resp():
    return flask.make_response(json.dumps({"error": ""})), 200


def need_login():
    return flask.make_response(
        json.dumps({"error": "You need to login to visit this page"})), 401
