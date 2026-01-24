import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartAEndB(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_starta_endb('acb'), 'Found a match!')

    def test_edge_case_no_a(self):
        self.assertEqual(text_starta_endb('bc'), 'Not matched!')

    def test_edge_case_no_b(self):
        self.assertEqual(text_starta_endb('ac'), 'Not matched!')

    def test_edge_case_only_a(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')

    def test_edge_case_only_b(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_typical_case_multiple_a_b(self):
        self.assertEqual(text_starta_endb('abcabc'), 'Found a match!')

    def test_typical_case_a_before_b(self):
        self.assertEqual(text_starta_endb('bca'), 'Not matched!')

    def test_typical_case_b_before_a(self):
        self.assertEqual(text_starta_endb('acb'), 'Found a match!')

    def test_typical_case_multiple_a_multiple_b(self):
        self.assertEqual(text_starta_endb('ababab'), 'Found a match!')

    def test_typical_case_a_and_b_together(self):
        self.assertEqual(text_starta_endb('abab'), 'Found a match!')

    def test_typical_case_a_and_b_together_with_other_chars(self):
        self.assertEqual(text_starta_endb('xabcy'), 'Found a match!')
