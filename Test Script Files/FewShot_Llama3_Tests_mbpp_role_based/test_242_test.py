import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_charac(""), 0)

    def test_single_character(self):
        self.assertEqual(count_charac("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_charac("abc"), 3)

    def test_string_with_spaces(self):
        self.assertEqual(count_charac("hello world"), 11)

    def test_string_with_punctuation(self):
        self.assertEqual(count_charac("Hello, World!"), 12)

    def test_string_with_numbers(self):
        self.assertEqual(count_charac("Hello123"), 7)
