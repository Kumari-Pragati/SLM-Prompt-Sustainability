import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_multiple_a(self):
        self.assertEqual(text_match('aa'), 'Not matched!')

    def test_multiple_ab(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_multiple_abab(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_multiple_ababab(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_multiple_ababab_with_space(self):
        self.assertEqual(text_match('abab abab'), 'Found a match!')

    def test_multiple_ababab_with_newline(self):
        self.assertEqual(text_match('abab\nabab'), 'Found a match!')

    def test_multiple_ababab_with_special_char(self):
        self.assertEqual(text_match('abab#abab'), 'Not matched!')

    def test_multiple_ababab_with_number(self):
        self.assertEqual(text_match('abab1abab'), 'Not matched!')
