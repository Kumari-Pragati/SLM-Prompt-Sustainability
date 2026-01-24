import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(odd_values_string("Hello"), "Hlo")

    def test_edge_case_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_edge_case_single_character_string(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_edge_case_even_length_string(self):
        self.assertEqual(odd_values_string("abcdef"), "ace")

    def test_edge_case_odd_length_string(self):
        self.assertEqual(odd_values_string("abcdefg"), "aceg")

    def test_edge_case_long_string(self):
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "acegikmoqsuwy")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            odd_values_string(123)
