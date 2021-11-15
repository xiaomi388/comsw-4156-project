import sqlite3

from werkzeug.datastructures import ImmutableMultiDict
from flask import Flask
import db
from os import error
import unittest
import json
import user

class TestUser(unittest.TestCase):
    def test_register_input_invalid(self):
        # email address format wrong
        mock_form = ImmutableMultiDict([('email', '123columbia.edu'), ('password', '12345'), ('name', 'testtestuser'),
                                        ('mobile_phone', '8148888477'), ('zipcode', '10026')])
        error, code = user.register(mock_form)
        self.assertEqual(code, 201)

    def test_register_sql_error(self):
        conn = None
        try:
            conn = sqlite3.connect('sqlite_db')
            mock_data_sql = "INSERT INTO User (email, password, name, zipcode, phone_number) " \
                            "VALUES ('123@columbia.edu', '12345', 'testtestuser', 10026, '8148888477');"

            mock_form = ImmutableMultiDict(
                [('email', '123@columbia.edu'), ('password', '12345'), ('name', 'testtestuser'),
                 ('mobile_phone', '8148888477'), ('zipcode', '10026')])

            conn.execute(mock_data_sql)
            conn.commit()

            error, code = user.register(mock_form)

            self.assertEqual(code, 500)

        except error as e:
            print(e)

        finally:
            if conn:
                conn.close()

    def test_user_login_happy_path(self):
        app = Flask(__name__)
        with app.app_context():
            email = "zj2304@columbia.edu"
            password = "passwd"
            resp, code = user.user_login(email, password)
            self.assertEqual(resp.data.decode("utf-8"), "{\"error\": \"\"}")
            self.assertEqual(code, 200)

    def test_user_login_no_such_email(self):
        email = "123@columbia.edu"
        password = "passwd"
        resp, code = user.user_login(email, password)
        self.assertEqual(resp, json.dumps({"error": f"No such email {email}"}))
        self.assertEqual(code, 400)

    def test_user_login_wrong_password(self):
        email = "zj2304@columbia.edu"
        password = "123"
        resp, code = user.user_login(email, password)
        self.assertEqual(resp,
                         json.dumps({"error": f"wrong password {email}"}))
        self.assertEqual(code, 400)

    def test_user_login_input_invalid(self):
        email = "zj2304@columbia.edu"
        password = None
        resp, code = user.user_login(email, password)
        self.assertEqual(resp, json.dumps({"error": "invalid input"}))
        self.assertEqual(code, 400)
