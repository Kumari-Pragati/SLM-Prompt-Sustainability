import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('a_b'), 'Found a match!')

    def test_edge_conditions(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('a_'), 'Not matched!')
        self.assertEqual(text_match('_b'), 'Not matched!')

    def test_complex_cases(self):
        self.assertEqual(text_match('a_b_c'), 'Not matched!')
        self.assertEqual(text_match('A_b'), 'Not matched!')
        self.assertEqual(text_match('a_B'), 'Not matched!')
        self.assertEqual(text_match('a_123'), 'Not matched!')
        self.assertEqual(text_match('a_b_c_d'), 'Not matched!')
