import json
import sqlite3
from wtforms import Form, validators, EmailField, PasswordField, StringField, FormField, IntegerField


class UserRegisterForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.length(min=8, max=30)])
    name = StringField('Username', [validators.DataRequired(), validators.length(min=6, max=30)])
    mobile_phone = StringField('Mobile', [validators.DataRequired(), validators.length(min=10, max=10)])
    zipcode = IntegerField('Zip', [validators.DataRequired()])


def register(raw_form):
    form = UserRegisterForm(raw_form)
    print(raw_form)
    if form.validate():
        user = [form.email.data, form.password.data, form.name.data, form.zipcode.data, form.mobile_phone.data]
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
