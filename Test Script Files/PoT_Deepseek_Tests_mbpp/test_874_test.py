import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Concat("abcabcabc", "abc"))

    def test_edge_case_empty_strings(self):
        self.assertTrue(check_Concat("", ""))

    def test_boundary_case_single_character(self):
        self.assertTrue(check_Concat("a", "a"))
        self.assertFalse(check_Concat("a", "b"))

    def test_corner_case_repeated_pattern(self):
        self.assertTrue(check_Concat("ababab", "ab"))

    def test_corner_case_non_repeated_pattern(self):
        self.assertFalse(check_Concat("abc", "def"))

    def test_corner_case_large_strings(self):
        self.assertTrue(check_Concat("a"*1000000, "a"))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            check_Concat(123, "abc")

    def test_invalid_input_empty_string_second(self):
        self.assertFalse(check_Concat("abc", ""))
