import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('acb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match('ab'), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match('a'*10000 + 'b'), 'Found a match!')

    def test_special_case(self):
        self.assertEqual(text_match('a'*10000 + 'b' + 'c'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
