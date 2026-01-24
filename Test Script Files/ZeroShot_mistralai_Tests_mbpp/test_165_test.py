import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_single_char_uppercase(self):
        self.assertEqual(count_char_position('A'), 1)

    def test_single_char_lowercase(self):
        self.assertEqual(count_char_position('a'), 1)

    def test_multiple_chars_uppercase(self):
        self.assertEqual(count_char_position('ABC'), 3)

    def test_multiple_chars_lowercase(self):
        self.assertEqual(count_char_position('abc'), 3)

    def test_mixed_case(self):
        self.assertEqual(count_char_position('AbCd'), 3)

    def test_special_characters(self):
        self.assertEqual(count_char_position('!@#$%^&*()_+-=[]{}|;:'\
                                              '\'<>,.?/'), 0)

    def test_whitespace(self):
        self.assertEqual(count_char_position('   '), 0)
