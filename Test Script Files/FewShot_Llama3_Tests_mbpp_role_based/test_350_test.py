import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(minimum_Length("abc"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(minimum_Length(""), 26)

    def test_edge_case_single_character(self):
        self.assertEqual(minimum_Length("a"), 25)

    def test_edge_case_all_same_characters(self):
        self.assertEqual(minimum_Length("aaaa"), 1)

    def test_edge_case_all_different_characters(self):
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            minimum_Length(123)
