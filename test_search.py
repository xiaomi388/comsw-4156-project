import unittest
import db
import search
import json


class Test_TestSearch(unittest.TestCase):
    def test_search_furniture_success(self):
        db.clear()
        db.init_db()
        db.populate_testing_data()
        keyword = "monitor"
        search_res = json.loads(search.search_furniture(keyword))
        self.assertEqual(len(search_res['furniture']), 1)
        self.assertEqual(search_res['furniture'][0]['owner'], 'Bob@gmail.com')
        self.assertEqual(search_res['furniture'][0]['labels'], 'monitor')

    def test_search_furniture_no_results(self):
        db.clear()
        db.init_db()
        keyword = "hikarunara"
        search_res = search.search_furniture(keyword)
        status_message, status_code = search_res
        self.assertEqual(status_code, 201)
        expected_error = {"error": "no matched furniture found"}
        self.assertEqual(status_message, json.dumps(expected_error))

    def test_search_furniture_non_keyword(self):
        db.clear()
        db.init_db()
        keyword = None
        search_res = search.search_furniture(keyword)
        status_message, status_code = search_res
        self.assertEqual(status_code, 400)
        expected_error = {"error": "keyword is empty"}
        self.assertEqual(status_message, json.dumps(expected_error))
