import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(text_match('abc_def'), 'Found a match!')

    def test_edge_condition(self):
        self.assertEqual(text_match('_abc_def'), 'Not matched!')

    def test_boundary_condition(self):
        self.assertEqual(text_match('abc_def_ghi'), 'Not matched!')

    def test_invalid_input(self):
        self.assertEqual(text_match('abc_123'), 'Not matched!')

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            text_match(123)
