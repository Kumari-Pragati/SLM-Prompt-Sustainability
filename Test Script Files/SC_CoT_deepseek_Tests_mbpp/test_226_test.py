import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_values_string("hello"), "hle")

    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_long_string(self):
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "acegikmouwy")

    def test_special_characters(self):
        self.assertEqual(odd_values_string("!@#$%^&*()"), "!@#%*")

    def test_numeric_string(self):
        self.assertEqual(odd_values_string("1234567890"), "13579")

    def test_whitespace_string(self):
        self.assertEqual(odd_values_string(" "), " ")
