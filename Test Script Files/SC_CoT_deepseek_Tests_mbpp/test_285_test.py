import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_two_three('abbb'), 'Found a match!')

    def test_edge_case_two(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')

    def test_edge_case_three(self):
        self.assertEqual(text_match_two_three('abb'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match_two_three('abbbbb'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_two_three('ac'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_two_three(123)
