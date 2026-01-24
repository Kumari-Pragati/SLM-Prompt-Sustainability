import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_charac(''), 0)

    def test_single_character_string(self):
        self.assertEqual(count_charac('a'), 1)

    def test_multiple_characters_string(self):
        self.assertEqual(count_charac('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(count_charac('hello world'), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(count_charac('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 33)

    def test_string_with_repeated_characters(self):
        self.assertEqual(count_charac('aaa'), 3)
