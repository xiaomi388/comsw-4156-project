import json
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
        db.clear()
        db.init_db()
        db.insert_mock_user()
        app = Flask(__name__)
        with app.app_context():
            mock_form = ImmutableMultiDict([
                ('email', 'zj2304@columbia.edu'),
                ('password', 'password')])
            resp, code, saved_user = user.user_login(mock_form)
            self.assertEqual(saved_user is not None, True)
            self.assertEqual(resp.data.decode("utf-8"), "{\"error\": \"\"}")
            self.assertEqual(code, 200)

    def test_user_login_no_such_email(self):
        db.clear()
        db.init_db()
        db.insert_mock_user()
        email = '888@columbia.edu'
        password = 'password'
        mock_form = ImmutableMultiDict([
            ('email', email),
            ('password', password)])
        resp, code, saved_user = user.user_login(mock_form)
        self.assertEqual(saved_user, None)
        self.assertEqual(resp, json.dumps({"error": f"No such email {email}"}))
        self.assertEqual(code, 400)

    def test_user_login_wrong_password(self):
        db.clear()
        db.init_db()
        db.insert_mock_user()
        email = "zj2304@columbia.edu"
        password = "12345678900"
        mock_form = ImmutableMultiDict([
            ('email', email),
            ('password', password)])
        resp, code, saved_user = user.user_login(mock_form)
        self.assertEqual(saved_user, None)
        self.assertEqual(resp,
                         json.dumps({"error": f"wrong password {email}"}))
        self.assertEqual(code, 400)

    def test_user_login_input_invalid(self):
        db.clear()
        db.init_db()
        db.insert_mock_user()
        email = "zj2304@columbia.edu"
        password = None
        mock_form = ImmutableMultiDict([
            ('email', email),
            ('password', password)])
        resp, code, saved_user = user.user_login(mock_form)
        self.assertEqual(saved_user, None)
        supposed_resp =\
            json.dumps({"error": "invalid input"})
        self.assertEqual(resp, supposed_resp)
        self.assertEqual(code, 400)

    def test_get_user_happy_path(self):
        db.clear()
        db.init_db()
        db.insert_mock_user()
        email = "zj2304@columbia.edu"
        saved_user = user.UserLoginObj.get(email)
        self.assertEqual(saved_user is not None, True)

    def test_get_user_empty_email(self):
        db.clear()
        db.init_db()
        db.insert_mock_user()
        email = ""
        saved_user = user.UserLoginObj.get(email)
        self.assertEqual(saved_user, None)

    def test_get_user_no_such_email(self):
        db.clear()
        db.init_db()
        db.insert_mock_user()
        email = "asdf@columbia.edu"
        saved_user = user.UserLoginObj.get(email)
        self.assertEqual(saved_user, None)
