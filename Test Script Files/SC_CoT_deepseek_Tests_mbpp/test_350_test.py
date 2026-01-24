import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum_Length('aabcb'), 3)

    def test_edge_case_single_char(self):
        self.assertEqual(minimum_Length('a'), 1)

    def test_edge_case_all_same_chars(self):
        self.assertEqual(minimum_Length('aaaaa'), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_corner_case_with_different_chars(self):
        self.assertEqual(minimum_Length('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            minimum_Length(123)

    def test_invalid_input_string_with_non_alphabet_chars(self):
        with self.assertRaises(ValueError):
            minimum_Length('abc123')
