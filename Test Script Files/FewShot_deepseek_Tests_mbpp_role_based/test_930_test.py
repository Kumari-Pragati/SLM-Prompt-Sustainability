import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match('a' * 10000 + 'b'), 'Found a match!')
        self.assertEqual(text_match('a' * 10001 + 'b'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
