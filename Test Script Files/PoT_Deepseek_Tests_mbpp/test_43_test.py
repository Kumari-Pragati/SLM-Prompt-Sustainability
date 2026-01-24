import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match('a_b'), 'Found a match!')
        self.assertEqual(text_match('abc_def'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('a_'), 'Not matched!')
        self.assertEqual(text_match('_b'), 'Not matched!')

    def test_corner_cases(self):
        self.assertEqual(text_match('A_b'), 'Not matched!')
        self.assertEqual(text_match('a_B'), 'Not matched!')
        self.assertEqual(text_match('a_1'), 'Found a match!')
        self.assertEqual(text_match('1_2'), 'Found a match!')
