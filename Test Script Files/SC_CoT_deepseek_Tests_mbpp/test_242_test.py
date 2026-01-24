import unittest

from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_charac('hello'), 5)

    def test_empty_string(self):
        self.assertEqual(count_charac(''), 0)

    def test_single_character(self):
        self.assertEqual(count_charac('a'), 1)

    def test_whitespace_string(self):
        self.assertEqual(count_charac(' '), 1)

    def test_special_characters(self):
        self.assertEqual(count_charac('!@#$%^&*()'), 10)

    def test_numeric_string(self):
        self.assertEqual(count_charac('1234567890'), 10)

    def test_long_string(self):
        self.assertEqual(count_charac('abcdefghijklmnopqrstuvwxyz' * 100), 3600)
