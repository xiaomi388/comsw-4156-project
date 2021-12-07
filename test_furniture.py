import unittest
import furniture
import json
import sqlite3
from unittest.mock import patch


class TestFurniture(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_post_furniture_happy_path(self, mock):
        params = None
        has_commit = False

        class MockConn:
            @staticmethod
            def execute(a, b):
                nonlocal params
                params = b

            @staticmethod
            def commit():
                nonlocal has_commit
                has_commit = True

            @staticmethod
            def close():
                pass

        mock.return_value = MockConn

        ret, code = furniture.create_furniture({
            "title": "mocktitle",
            "labels": "mocklabel",
            "image_url": "mockurl",
            "description": "mockdesc"}, "mockuser")

        self.assertEqual(code, 201)
        self.assertEqual(ret, json.dumps({"error": ""}))
        self.assertEqual(
            params,
            ["mockuser", "mocktitle", "mocklabel", "mockurl", "mockdesc"]
        )
        self.assertTrue(has_commit)

    def test_post_furniture_input_invalid(self):
        tests = [
            {"invalid_field": "invalid"},
            {
                "title": 255,
                "labels": "invalid type",
                "image_url": "xxx",
                "description": "sss"
            },
            {"title": "missing some fields"}
        ]
        for test in tests:
            ret, code = furniture.create_furniture(test, "mockuser")

            self.assertEqual(ret, json.dumps({"error": "input invalid."}))
            self.assertEqual(code, 400)

    @patch('sqlite3.connect')
    def test_post_furniture_sql_error(self, mock):
        mock.side_effect = sqlite3.Error("mockerr")

        ret, code = furniture.create_furniture({
            "title": "mockt",
            "labels": "mocklabel",
            "image_url": "xxx",
            "description": "sss"}, "mockuser")

        self.assertEqual(code, 500)
        self.assertEqual(ret, json.dumps({"error": "db error: mockerr"}))

    @patch('sqlite3.connect')
    def test_rate_buyer_happy_path(self, mock):
        class MockCursor:
            @staticmethod
            def fetchone():
                return ["realbuyer@gmail.com", "owner@gmail.com", "completed"]

        class MockConn:
            def __init__(self):
                self.exec_cnt = 0
                self.params = []
                self.has_commit = None

            def execute(self, a, b):
                self.exec_cnt += 1
                self.params.append(b)
                if self.exec_cnt == 1:
                    return MockCursor

            def commit(self):
                self.has_commit = True

            def close(self):
                pass

        mock.return_value = MockConn()
        ret, code = furniture.rate_owner("mockfid", "realbuyer@gmail.com", 5)

        self.assertEqual(ret, json.dumps({"error": ""}))
        self.assertEqual(code, 200)
        self.assertEqual(mock.return_value.exec_cnt, 3)
        self.assertEqual(mock.return_value.params,
                         [["mockfid"], [5, "owner@gmail.com"], ["mockfid"]])
        self.assertEqual(mock.return_value.has_commit, True)

    @patch('sqlite3.connect')
    def test_rate_buyer_client_error(self, mock):
        class MockCursor:
            def __init__(self, rec):
                self.rec = rec

            def fetchone(self):
                return self.rec

        class MockConn:
            def __init__(self, rec):
                self.rec = rec
                self.has_commit = False

            def execute(self, a, b):
                return MockCursor(self.rec)

            def close(self):
                pass

        for fid, buyer_email, rating, dbrec, exp_msg in [
            (
                    "", "", 10000, None,
                    "rating score should be in the range of [0, 5]"
            ),
            (
                    "", "", -1, None,
                    "rating score should be in the range of [0, 5]"
            ),
            (
                    "mockfid", "111@gmail.com", 5, None,
                    "fid not existed"
            ),
            (
                    "mockfid", "111@gmail.com", 5,
                    ("111@gmail.com", "", "pending"),
                    "please rate after the transaction is completed"
            ),
            (
                    "mockfid", "111@gmail.com", 5,
                    ("222@gmail.com", "", "completed"),
                    "rating can only be triggered by the buyer"
            ),
            (
                    "mockfid", "111@gmail.com", 5,
                    ("111@gmail.com", "", "rated"),
                    "this transaction has been rated"
            ),
        ]:
            mock.return_value = MockConn(dbrec)

            ret, code = furniture.rate_owner(fid, buyer_email, rating)
            ret = json.loads(ret)

            self.assertEqual(code, 400)
            self.assertEqual(ret["error"], exp_msg)
            self.assertFalse(mock.return_value.has_commit)

    @patch('sqlite3.connect')
    def test_rate_buyer_sql_error(self, mock):
        mock.side_effect = sqlite3.Error("mockerr")

        ret, code = furniture.rate_owner("fid", "buyer", 5)

        self.assertEqual(code, 500)
        self.assertEqual(ret, json.dumps({"error": "db error: mockerr"}))
