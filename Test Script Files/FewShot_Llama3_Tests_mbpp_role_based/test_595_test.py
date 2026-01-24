import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_Swaps("abc", "abd"), 1)

    def test_edge_case_equal_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)

    def test_edge_case_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)

    def test_edge_case_single_character_strings(self):
        self.assertEqual(min_Swaps("a", "a"), 0)

    def test_edge_case_long_strings(self):
        self.assertEqual(min_Swaps("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"), 25)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, "abc")

    def test_invalid_input_length(self):
        with self.assertRaises(TypeError):
            min_Swaps("abc", "abcd")
