import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_two_three('abbb'), 'Found a match!')
        self.assertEqual(text_match_two_three('abbbb'), 'Found a match!')
        self.assertEqual(text_match_two_three('abbbbb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_two_three('ab'), 'Not matched!')
        self.assertEqual(text_match_two_three('abb'), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_two_three('abbbbbb'), 'Found a match!')
        self.assertEqual(text_match_two_three('abbbbbbb'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_two_three(123)
