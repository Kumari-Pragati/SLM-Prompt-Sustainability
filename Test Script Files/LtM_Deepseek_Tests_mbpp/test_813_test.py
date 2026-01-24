import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(string_length("hello"), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_string_with_spaces(self):
        self.assertEqual(string_length("hello world"), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(string_length("hello@world"), 10)

    def test_string_with_numbers(self):
        self.assertEqual(string_length("12345"), 5)
