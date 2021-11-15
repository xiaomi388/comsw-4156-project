from flask import request, jsonify
import json
import sqlite3
from wtforms import Form, validators,EmailField, PasswordField, StringField,FormField, IntegerField
from wtforms.validators import DataRequired,DataRequired, Email,EqualTo,length
import jsonschema
import json
import flask
import sqlite3
import userDB

'''class USMobileForm(Form):
    area_code = IntegerField('Area Code', validators = [DataRequired(), length(min = 3, max = 3)])
    exchange = IntegerField('Exchange', validators=[DataRequired(), length(min=3, max=3)])
    line_number = IntegerField('Number', validators=[DataRequired(), length(min=4, max=4)])'''


class UserRegisterForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    #password = PasswordField('Password', [DataRequired(), EqualTo('confirm',message='Passwords must match')])
    #confirm = PasswordField('Confirm Password')
    password = PasswordField('Password', [validators.DataRequired()])
    name = StringField('Username', [validators.DataRequired(),validators.length(min=6, max=30)])
    mobile_phone = StringField('Mobile', [validators.DataRequired(), validators.length(min=10, max=10)])
    zipcode = StringField('Zipcode', [validators.DataRequired(), validators.length(min=5, max=5)])


def register(raw_form):
    form = UserRegisterForm(raw_form)
    print(raw_form)
    if form.validate():
        user = [form.email.data, form.password.data, form.name.data, form.zipcode.data, form.mobile_phone.data]
        #wirte data to db
        conn = None
        try:
            conn = sqlite3.connect("sqlite_db")
            conn.execute(
                "INSERT INTO User "
                "(email, password, name, zipcode, phone_number) "
                "VALUES (?, ?, ?, ?, ?)", user
            )
            conn.commit()
        except sqlite3.Error as e:
            return json.dumps({"error": f"db error: {str(e)}"}), 500
        finally:
            if conn:
                conn.close()
    return json.dumps({"error": form.errors}), 201
    #jsonify(form.errors), 400

def set_user_cookie(email:str, resp):
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
    except :
        return json.dumps({"error": f"Internal error"}), 500

