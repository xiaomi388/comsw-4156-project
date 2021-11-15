import db
from wtforms import Form, validators, EmailField, PasswordField, StringField, IntegerField
import json
import flask
import sqlite3
import userDB


class UserRegisterForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(),validators.length(min=8, max=30)])
    name = StringField('Username', [validators.DataRequired(), validators.length(min=3, max=30)])
    mobile_phone = StringField('Mobile', [validators.DataRequired(), validators.length(min=10, max=10)])
    zipcode = IntegerField('Zipcode', [validators.DataRequired()])


def register(raw_form):
    form = UserRegisterForm(raw_form)
    #print(raw_form)
    if not form.validate():
        return json.dumps({"Input error": form.errors}), 400

    user = (form.email.data, form.password.data, form.name.data, form.zipcode.data, form.mobile_phone.data)
    # wirte data to db
    conn = None
    try:
        conn = sqlite3.connect("sqlite_db")
        cur = conn.cursor()
        sql = "INSERT INTO User(email, password, name, zipcode, phone_number) VALUES(?, ?, ?, ?, ?) "
        cur.execute(sql, user)
        conn.commit()
    except sqlite3.Error as e:
        return json.dumps({"error": f"db error: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
    return json.dumps({"error": ""}), 201


def set_user_cookie(email: str, resp):
    resp.set_cookie('user', email)


def need_login_response():
    return json.dumps({"error": f"Please login first"}), 400


def user_login(req):
    # integrity check
    print(req.endpoint)
    try:
        email = req.args.get("email")
        password = req.args.get("password")
        print(email, password)
        saved_user = userDB.select_user_by_email(email)
        print(saved_user)
        if not saved_user:
            return json.dumps({"error": f"No such email {str(email)}"}), 400
        # To Do: md5
        if not password == saved_user.get_password():
            return json.dumps({"error": f"wrong password {str(email)}"}), 400
        resp = flask.make_response(json.dumps({"error": ""}))
        set_user_cookie(email, resp)
        return resp, 200
    except:
        return json.dumps({"error": f"Internal error"}), 500
