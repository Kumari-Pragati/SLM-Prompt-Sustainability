import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_Concat("abc", "abc"))
        self.assertTrue(check_Concat("abcd", "abcd"))
        self.assertTrue(check_Concat("a", "a"))

    def test_edge_case_short_str1(self):
        self.assertFalse(check_Concat("abc", "xyz"))
        self.assertFalse(check_Concat("", "xyz"))

    def test_edge_case_short_str2(self):
        self.assertFalse(check_Concat("abc", "a"))
        self.assertFalse(check_Concat("abc", ""))

    def test_edge_case_equal_length(self):
        self.assertTrue(check_Concat("abc", "def"))
        self.assertTrue(check_Concat("abc", "abcdef"))

    def test_corner_case_empty_strings(self):
        self.assertTrue(check_Concat("", ""))

    def test_corner_case_one_string_empty(self):
        self.assertFalse(check_Concat("", "abc"))
