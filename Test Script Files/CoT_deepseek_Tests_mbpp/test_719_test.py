import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abb'), 'Found a match!')
        self.assertEqual(text_match('abbb'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('aab'), 'Not matched!')
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            text_match(123)
        with self.assertRaises(TypeError):
            text_match(None)
        with self.assertRaises(TypeError):
            text_match(True)
