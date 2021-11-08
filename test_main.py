import unittest
import main


class TestFoo(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(main.foo(10, 20), 30)
