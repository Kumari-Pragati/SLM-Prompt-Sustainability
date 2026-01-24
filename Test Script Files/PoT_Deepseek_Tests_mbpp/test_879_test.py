import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('acb'), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match(''), 'Not matched!')

    def test_corner_case(self):
        self.assertEqual(text_match('abc'), 'Not matched!')
        self.assertEqual(text_match('aabc'), 'Not matched!')
        self.assertEqual(text_match('acbabc'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
