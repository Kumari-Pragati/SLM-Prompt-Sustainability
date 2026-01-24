import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_Concat("abc", "abc"))
        self.assertTrue(check_Concat("aabcc", "abc"))

    def test_edge_case_short_str1(self):
        self.assertFalse(check_Concat("ab", "abc"))

    def test_edge_case_short_str2(self):
        self.assertFalse(check_Concat("abc", "ab"))

    def test_edge_case_empty_str(self):
        self.assertTrue(check_Concat("", ""))
        self.assertFalse(check_Concat("abc", ""))
        self.assertFalse(check_Concat("", "abc"))

    def test_edge_case_one_char_str(self):
        self.assertTrue(check_Concat("a", "a"))

    def test_edge_case_only_spaces(self):
        self.assertTrue(check_Concat("   ", "   "))
        self.assertFalse(check_Concat("abc", "   "))
        self.assertFalse(check_Concat("   ", "abc"))

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, check_Concat, 123, "abc")
        self.assertRaises(TypeError, check_Concat, "abc", 123)
