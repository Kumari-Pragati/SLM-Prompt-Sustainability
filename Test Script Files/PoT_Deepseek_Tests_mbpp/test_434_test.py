import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')

    def test_edge_case_single_character(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')

    def test_boundary_case_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_corner_case_multiple_a_no_b(self):
        self.assertEqual(text_match_one('aaaa'), 'Not matched!')

    def test_corner_case_multiple_b_no_a(self):
        self.assertEqual(text_match_one('bbbb'), 'Not matched!')

    def test_corner_case_multiple_a_and_b(self):
        self.assertEqual(text_match_one('abababab'), 'Found a match!')

    def test_corner_case_single_b_before_a(self):
        self.assertEqual(text_match_one('ba'), 'Not matched!')

    def test_corner_case_single_b_after_a(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')
