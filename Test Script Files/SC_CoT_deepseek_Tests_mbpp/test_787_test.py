import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_three('abbb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_three('abbbb'), 'Found a match!')

    def test_special_case(self):
        self.assertEqual(text_match_three('abbba'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_three(123)
