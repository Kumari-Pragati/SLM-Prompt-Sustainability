import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_single_char(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_same_char_count(self):
        self.assertEqual(get_max_occuring_char('aab'), 'a')

    def test_different_char_count(self):
        self.assertEqual(get_max_occuring_char('aabbc'), 'b')

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_string_with_spaces(self):
        self.assertEqual(get_max_occuring_char('a b c'), ' ')

    def test_string_with_special_chars(self):
        self.assertEqual(get_max_occuring_char('a!b@c#'), '!')
