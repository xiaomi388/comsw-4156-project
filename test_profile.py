from os import error
import unittest
import profile
import json
import sqlite3
from unittest.mock import patch


class TestProfile(unittest.TestCase):
    def test_get_profile_input_invalid(self):


        conn = None
        try:
            conn = sqlite3.connect('sqlite_db')

            cur = conn.cursor()

            mock_data_sql = 'INSERT OR IGNORE INTO USER ' + '(email, password, name, ' +\
                    'zipcode, rating, transcation_count, phone_number) ' +\
                    'VALUES (\'test0@email.com\', \'123\', \'rick\', 100000, 5, 1, \'123123\');'
            print(mock_data_sql)
            cur.execute(mock_data_sql)
            conn.commit()

            print('Database Online, a mock user has been inserted.')

            test_res = profile.get_profile("test0@email.com")
            exp_res = '{"profile": {"email": "test0@email.com", "name": "rick", "zipcode": 100000, "phone_number": "123123"}}'
            self.assertEqual(exp_res, test_res)

        except error as e:
            print(e)

        finally:
            if conn:
                conn.close()