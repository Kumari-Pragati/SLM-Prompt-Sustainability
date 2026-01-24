import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_edge_case_with_no_match(self):
        self.assertEqual(text_match('ac'), 'Not matched!')

    def test_edge_case_with_single_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_edge_case_with_single_b(self):
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_typical_case_with_multiple_a_and_b(self):
        self.assertEqual(text_match('abbabababab'), 'Found a match!')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_edge_case_with_very_long_string(self):
        self.assertEqual(text_match('a' * 10000 + 'b'), 'Found a match!')
