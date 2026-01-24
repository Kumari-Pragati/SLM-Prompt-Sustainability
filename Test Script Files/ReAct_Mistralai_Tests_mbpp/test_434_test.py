import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_match_one('b'), 'Not matched!')

    def test_multiple_a(self):
        self.assertEqual(text_match_one('aa'), 'Not matched!')

    def test_multiple_ab(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')

    def test_multiple_ab_with_spaces(self):
        self.assertEqual(text_match_one('ab   '), 'Found a match!')

    def test_multiple_ab_with_newline(self):
        self.assertEqual(text_match_one('ab\n'), 'Found a match!')

    def test_multiple_ab_with_special_characters(self):
        self.assertEqual(text_match_one('ab!'), 'Not matched!')

    def test_long_string_with_match(self):
        long_string = 'a' * 100 + 'b' * 100
        self.assertEqual(text_match_one(long_string), 'Found a match!')

    def test_long_string_without_match(self):
        long_string = 'a' * 100 + 'c' * 100
        self.assertEqual(text_match_one(long_string), 'Not matched!')
