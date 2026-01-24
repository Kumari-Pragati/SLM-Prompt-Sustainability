import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('ababababab'), 'Found a match!')

    def test_corner_case(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('ba'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
        with self.assertRaises(TypeError):
            text_match(None)
