import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(text_starta_endb("starta1234567890endb"), 'Found a match!')

    def test_edge_case_longer(self):
        self.assertEqual(text_starta_endb("starta1234567890xtraendb"), 'Found a match!')

    def test_edge_case_shorter(self):
        self.assertEqual(text_starta_endb("starta123endb"), 'Found a match!')

    def test_edge_case_no_a(self):
        self.assertEqual(text_starta_endb("b1234567890endb"), 'Not matched!')

    def test_edge_case_no_b(self):
        self.assertEqual(text_starta_endb("startac1234567890"), 'Not matched!')

    def test_edge_case_no_a_or_b(self):
        self.assertEqual(text_starta_endb("1234567890"), 'Not matched!')

    def test_edge_case_multiple_a(self):
        self.assertEqual(text_starta_endb("startaa1234567890endb"), 'Found a match!')

    def test_edge_case_multiple_b(self):
        self.assertEqual(text_starta_endb("starta1234567890endbb"), 'Not matched!')

    def test_edge_case_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb("startaa1234567890endbb"), 'Not matched!')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            text_starta_endb(123)
