import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_with_a_and_b(self):
        self.assertEqual(text_match('aaab'), 'Found a match!')

    def test_match_with_multiple_a_and_b(self):
        self.assertEqual(text_match('aaaaabbbbb'), 'Found a match!')

    def test_match_with_only_a_and_b(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_no_match_with_no_a_or_b(self):
        self.assertEqual(text_match('ccc'), 'Not matched!')

    def test_no_match_with_a_before_b(self):
        self.assertEqual(text_match('ba'), 'Not matched!')

    def test_no_match_with_b_before_a(self):
        self.assertEqual(text_match('abaa'), 'Not matched!')

    def test_no_match_with_no_a_and_multiple_b(self):
        self.assertEqual(text_match('bbbb'), 'Not matched!')
