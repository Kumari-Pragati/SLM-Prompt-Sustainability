import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_two_three('abbb'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_two_three(''), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_match_two_three('ac'), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_two_three('abbbab'), 'Found a match!')
