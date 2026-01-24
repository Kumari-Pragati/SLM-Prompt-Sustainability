import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match('acb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match('a' * 10000 + 'b'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
