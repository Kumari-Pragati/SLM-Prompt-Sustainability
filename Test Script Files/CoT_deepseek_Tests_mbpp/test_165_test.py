import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char_position('ABC'), 3)
        self.assertEqual(count_char_position('abc'), 3)
        self.assertEqual(count_char_position('AbC'), 3)

    def test_single_character(self):
        self.assertEqual(count_char_position('A'), 1)
        self.assertEqual(count_char_position('a'), 1)

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_special_characters(self):
        self.assertEqual(count_char_position('!@#'), 0)
        self.assertEqual(count_char_position('123'), 0)

    def test_numeric_string(self):
        self.assertEqual(count_char_position('123456'), 0)

    def test_whitespace_string(self):
        self.assertEqual(count_char_position(' '), 0)
        self.assertEqual(count_char_position('   '), 0)

    def test_string_with_special_characters(self):
        self.assertEqual(count_char_position('A!@#'), 1)
        self.assertEqual(count_char_position('a123'), 1)
