import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_length('Hello'), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(''), 0)

    def test_string_with_spaces(self):
        self.assertEqual(string_length('Hello World'), 10)

    def test_string_with_special_characters(self):
        self.assertEqual(string_length('Hello@World'), 10)

    def test_string_with_numbers(self):
        self.assertEqual(string_length('12345'), 5)

    def test_string_with_mixed_characters(self):
        self.assertEqual(string_length('H3ll0'), 4)

    def test_string_with_long_text(self):
        self.assertEqual(string_length('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'), 100)
