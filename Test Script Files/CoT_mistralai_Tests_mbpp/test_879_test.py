import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_with_a_and_b(self):
        self.assertEqual(text_match('aaab'), 'Found a match!')

    def test_match_with_multiple_a_and_b(self):
        self.assertEqual(text_match('aaaaabbbbb'), 'Found a match!')

    def test_match_at_beginning_of_string(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_at_end_of_string(self):
        self.assertEqual(text_match('aaab'), 'Found a match!')

    def test_match_in_middle_of_string(self):
        self.assertEqual(text_match('aaaabbb'), 'Found a match!')

    def test_match_with_multiple_a_and_b_in_middle(self):
        self.assertEqual(text_match('aaaabbbaaa'), 'Found a match!')

    def test_no_match_when_no_b(self):
        self.assertEqual(text_match('aaa'), 'Not matched!')

    def test_no_match_when_no_a(self):
        self.assertEqual(text_match('bbb'), 'Not matched!')

    def test_no_match_when_a_before_b(self):
        self.assertEqual(text_match('ba'), 'Not matched!')

    def test_no_match_when_b_before_a(self):
        self.assertEqual(text_match('ab'), 'Not matched!')

    def test_no_match_when_no_a_or_b(self):
        self.assertEqual(text_match(''), 'Not matched!')
