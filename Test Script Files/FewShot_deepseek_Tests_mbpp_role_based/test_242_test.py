import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_charac("Hello"), 5)

    def test_empty_string(self):
        self.assertEqual(count_charac(""), 0)

    def test_string_with_spaces(self):
        self.assertEqual(count_charac("Hello World"), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(count_charac("Hello@World"), 10)

    def test_string_with_numbers(self):
        self.assertEqual(count_charac("12345"), 5)
