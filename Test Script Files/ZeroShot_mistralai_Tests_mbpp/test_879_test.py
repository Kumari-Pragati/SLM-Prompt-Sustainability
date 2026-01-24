import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_single_ab(self):
        self.assertEqual(text_match('ab'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_match('aaabbb'), 'Found a match!')

    def test_multiple_a_and_non_b(self):
        self.assertEqual(text_match('aaaccc'), 'Not matched!')

    def test_multiple_b_and_non_a(self):
        self.assertEqual(text_match('bbbbb'), 'Not matched!')

    def test_multiple_a_and_b_with_other_chars(self):
        self.assertEqual(text_match('aaabbbccc'), 'Not matched!')

    def test_multiple_a_and_b_with_spaces(self):
        self.assertEqual(text_match('aaa bbb'), 'Not matched!')
