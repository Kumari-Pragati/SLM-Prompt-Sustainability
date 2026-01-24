import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('aaab'), 'Found a match!')

    def test_min_length_match(self):
        self.assertEqual(text_match('a'), 'Found a match!')

    def test_max_length_match(self):
        self.assertEqual(text_match('aaaaaaaaaaaaaaaaab'), 'Found a match!')

    def test_edge_case_match(self):
        self.assertEqual(text_match('a\nb'), 'Found a match!')

    def test_empty_input(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_no_b_in_input(self):
        self.assertEqual(text_match('aaa'), 'Not matched!')

    def test_no_a_in_input(self):
        self.assertEqual(text_match('bbb'), 'Not matched!')

    def test_multiple_a_before_b(self):
        self.assertEqual(text_match('aaaaab'), 'Not matched!')

    def test_multiple_b_after_a(self):
        self.assertEqual(text_match('aabbb'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_match('aaabbb'), 'Not matched!')
