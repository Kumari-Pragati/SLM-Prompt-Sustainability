import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_carol(2), 14)

    def test_zero_input(self):
        self.assertEqual(get_carol(0), 0)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            get_carol(-1)

    def test_large_input(self):
        with self.assertRaises(Exception):
            get_carol(1000)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            get_carol(2.5)

    def test_string_input(self):
        with self.assertRaises(Exception):
            get_carol("two")
