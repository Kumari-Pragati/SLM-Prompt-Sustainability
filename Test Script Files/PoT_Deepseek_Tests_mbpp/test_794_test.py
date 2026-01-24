import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartAEndB(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_starta_endb('ab'), 'Found a match!')

    def test_edge_case_single_character(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_boundary_case_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_corner_case_multiple_characters(self):
        self.assertEqual(text_starta_endb('acb'), 'Not matched!')
        self.assertEqual(text_starta_endb('aabb'), 'Not matched!')
        self.assertEqual(text_starta_endb('abab'), 'Not matched!')

    def test_tricky_case_no_a_or_b(self):
        self.assertEqual(text_starta_endb('xyz'), 'Not matched!')

    def test_tricky_case_a_after_b(self):
        self.assertEqual(text_starta_endb('bba'), 'Not matched!')

    def test_tricky_case_b_before_a(self):
        self.assertEqual(text_starta_endb('abab'), 'Not matched!')
