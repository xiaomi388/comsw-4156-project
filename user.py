from flask import request, jsonify
import json
import sqlite3
from wtforms import Form, validators,EmailField, PasswordField, StringField,FormField, IntegerField
from wtforms.validators import DataRequired,DataRequired, Email,EqualTo,length


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
    return jsonify(form.errors), 400
