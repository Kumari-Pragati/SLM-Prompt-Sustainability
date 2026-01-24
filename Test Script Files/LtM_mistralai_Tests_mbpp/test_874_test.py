import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_simple_concat(self):
        self.assertTrue(check_Concat("abc", "abc"))
        self.assertTrue(check_Concat("a", "a"))
        self.assertTrue(check_Concat("aa", "aa"))
        self.assertTrue(check_Concat("abcd", "abcd"))

    def test_edge_cases(self):
        self.assertFalse(check_Concat("", ""))
        self.assertFalse(check_Concat("a", ""))
        self.assertFalse(check_Concat("", "b"))
        self.assertFalse(check_Concat("a", "b"))
        self.assertTrue(check_Concat("abc", "ab"))
        self.assertFalse(check_Concat("abcd", "ab"))
        self.assertTrue(check_Concat("abc", "abcd"))
        self.assertFalse(check_Concat("abcd", "abc"))

    def test_complex_cases(self):
        self.assertTrue(check_Concat("aaa", "a"))
        self.assertFalse(check_Concat("aaa", "b"))
        self.assertTrue(check_Concat("aaab", "aa"))
        self.assertFalse(check_Concat("aaab", "ab"))
        self.assertTrue(check_Concat("aaab", "aba"))
