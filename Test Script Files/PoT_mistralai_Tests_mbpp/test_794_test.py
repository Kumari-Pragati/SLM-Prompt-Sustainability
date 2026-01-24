import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_starta_endb("hello_world_a_b"), 'Found a match!')

    def test_edge_case_longer(self):
        self.assertEqual(text_starta_endb("hello_world_a_b_c"), 'Not matched!')

    def test_edge_case_shorter(self):
        self.assertEqual(text_starta_endb("a_b"), 'Found a match!')

    def test_boundary_case_start_with_space(self):
        self.assertEqual(text_starta_endb(" a_b"), 'Found a match!')

    def test_boundary_case_end_with_space(self):
        self.assertEqual(text_starta_endb("a_b "), 'Not matched!')

    def test_boundary_case_start_end_with_space(self):
        self.assertEqual(text_starta_endb(" a_b "), 'Not matched!')

    def test_boundary_case_only_a(self):
        self.assertEqual(text_starta_endb("a"), 'Not matched!')

    def test_boundary_case_only_b(self):
        self.assertEqual(text_starta_endb("b"), 'Not matched!')

    def test_boundary_case_no_a(self):
        self.assertEqual(text_starta_endb("hello_world_b"), 'Not matched!')

    def test_boundary_case_no_b(self):
        self.assertEqual(text_starta_endb("hello_world_a"), 'Not matched!')
