import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('b'), 'Not matched!')
        self.assertEqual(text_match('ac'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('a' * 10000 + 'b'), 'Found a match!')
        self.assertEqual(text_match('b' * 10000 + 'a'), 'Not matched!')

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            text_match(123)
        with self.assertRaises(TypeError):
            text_match(['ab'])
