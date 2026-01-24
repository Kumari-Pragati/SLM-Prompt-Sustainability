import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_edge_case_with_only_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_edge_case_with_only_b(self):
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_corner_case_with_multiple_characters(self):
        self.assertEqual(text_match('ac'), 'Not matched!')

    def test_corner_case_with_ab(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_corner_case_with_a_followed_by_b(self):
        self.assertEqual(text_match('aab'), 'Not matched!')

    def test_corner_case_with_multiple_b_before_a(self):
        self.assertEqual(text_match('bbba'), 'Not matched!')

    def test_corner_case_with_multiple_a_before_b(self):
        self.assertEqual(text_match('aabba'), 'Not matched!')

    def test_corner_case_with_multiple_a_and_b(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_corner_case_with_multiple_b_and_a(self):
        self.assertEqual(text_match('baabab'), 'Found a match!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            text_match(123)
