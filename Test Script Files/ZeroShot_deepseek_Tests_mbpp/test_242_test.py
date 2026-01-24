import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_charac(''), 0)

    def test_single_character(self):
        self.assertEqual(count_charac('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_charac('abc'), 3)

    def test_special_characters(self):
        self.assertEqual(count_charac('!@#$%^&*()'), 9)

    def test_whitespace(self):
        self.assertEqual(count_charac(' '), 1)
