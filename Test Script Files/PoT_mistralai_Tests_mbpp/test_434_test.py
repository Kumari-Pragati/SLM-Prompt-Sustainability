import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')
        self.assertEqual(text_match_one('aab'), 'Found a match!')
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_edge_case_single_a(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_edge_case_no_b(self):
        self.assertEqual(text_match_one('ac'), 'Not matched!')

    def test_edge_case_multiple_b(self):
        self.assertEqual(text_match_one('bb'), 'Not matched!')

    def test_corner_case_single_ab(self):
        self.assertEqual(text_match_one('ababab'), 'Found a match!')
