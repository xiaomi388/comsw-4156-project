import json
import sqlite3
from flask import Flask
import db
from werkzeug.datastructures import ImmutableMultiDict
import unittest
import user


class TestUser(unittest.TestCase):
    def test_register_happy_path(self):
        db.clear()
        db.init_db()
        mock_form = ImmutableMultiDict([
            ('email', '456@columbia.edu'),
            ('password', '12345678'),
            ('name', 'testtestuser'),
            ('mobile_phone', '8148888477'),
            ('zipcode', 10026)])

        ret, code = user.register(mock_form)

        self.assertEqual(code, 201)
        self.assertEqual(ret, json.dumps({"error": ""}))

    def test_register_input_invalid(self):
        db.clear()
        db.init_db()
        #invalid input, email format, password length, name length
        mock_form = ImmutableMultiDict([
            ('email', '123columbia.edu'),
            ('password', '12345'),
            ('name', 'te'),
            ('mobile_phone', '8148888477'),
            ('zipcode', 10026)])
        error, code = user.register(mock_form)
        self.assertEqual(code, 400)

    def test_register_sql_error(self):
        db.clear()
        db.init_db()
        mock_form0 = ImmutableMultiDict([
            ('email', '456@columbia.edu'),
            ('password', '12345678'),
            ('name', 'testtestuser'),
            ('mobile_phone', '8148888477'),
            ('zipcode', 10026)])
        user.register(mock_form0)
        mock_form = ImmutableMultiDict([
            ('email', '456@columbia.edu'),
            ('password', '12345678'),
            ('name', 'testtestuser'),
            ('mobile_phone', '8148888477'),
            ('zipcode', 10026)])
        error, code = user.register(mock_form)
        self.assertEqual(code, 500)


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
