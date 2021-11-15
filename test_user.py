import sqlite3
from werkzeug.datastructures import ImmutableMultiDict
import unittest
import user

class TestUser(unittest.TestCase):

    def test_register_input_invalid(self):
        #email address format wrong
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

            mock_form = ImmutableMultiDict([('email', '123@columbia.edu'), ('password', '12345'), ('name', 'testtestuser'),
                                ('mobile_phone', '8148888477'), ('zipcode', '10026')])

            conn.execute(mock_data_sql)
            conn.commit()

            error,code = user.register(mock_form)

            self.assertEqual(code, 500)

        except error as e:
            print(e)

        finally:
            if conn:
                conn.close()

