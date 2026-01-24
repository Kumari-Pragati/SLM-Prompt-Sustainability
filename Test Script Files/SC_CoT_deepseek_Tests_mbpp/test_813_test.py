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

    def test_string_with_mixed_case(self):
        self.assertEqual(string_length('HelloWorld'), 10)

    def test_string_with_upper_case(self):
        self.assertEqual(string_length('HELLO'), 5)

    def test_string_with_lower_case(self):
        self.assertEqual(string_length('hello'), 5)
