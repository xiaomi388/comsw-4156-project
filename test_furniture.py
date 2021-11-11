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

        mock.return_value = MockConn

        ret, code = furniture.create_furniture({
            "title": "mocktitle",
            "labels": "mocklabel",
            "image_url": "mockurl",
            "description": "mockdesc"}
        )

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
            ret, code = furniture.create_furniture(test)

            self.assertEqual(ret, json.dumps({"error": "input invalid."}))
            self.assertEqual(code, 400)

    @patch('sqlite3.connect')
    def test_post_furniture_sql_error(self, mock):
        mock.side_effect = sqlite3.Error("mockerr")

        ret, code = furniture.create_furniture({
            "title": "mockt",
            "labels": "mocklabel",
            "image_url": "xxx",
            "description": "sss"}
        )

        self.assertEqual(code, 500)
        self.assertEqual(ret, json.dumps({"error": "db error: mockerr"}))
