import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Concat("abcabcabc", "abc"))

    def test_edge_case_empty_strings(self):
        self.assertTrue(check_Concat("", ""))

    def test_edge_case_one_char_strings(self):
        self.assertTrue(check_Concat("a", "a"))
        self.assertFalse(check_Concat("a", "b"))

    def test_edge_case_long_strings(self):
        self.assertTrue(check_Concat("a"*1000000, "a"))

    def test_error_case_different_lengths(self):
        self.assertFalse(check_Concat("abc", "abcd"))

    def test_error_case_different_content(self):
        self.assertFalse(check_Concat("abcabcabc", "abd"))
