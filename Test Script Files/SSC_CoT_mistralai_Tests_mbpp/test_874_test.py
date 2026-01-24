import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(check_Concat("abc", "abc"))
        self.assertTrue(check_Concat("abcd", "abcd"))
        self.assertTrue(check_Concat("a", "a"))

    def test_edge_case(self):
        self.assertFalse(check_Concat("abcd", "abc"))
        self.assertFalse(check_Concat("abc", "abcd"))
        self.assertFalse(check_Concat("", ""))
        self.assertFalse(check_Concat("abc", "def"))
        self.assertFalse(check_Concat("abc", "abcdx"))

    def test_boundary_case(self):
        self.assertTrue(check_Concat("a", "a"))
        self.assertTrue(check_Concat("aa", "a"))
        self.assertTrue(check_Concat("abcd", "abcd"))
        self.assertTrue(check_Concat("abcd", "abcdabcd"))
        self.assertFalse(check_Concat("abcd", "abcdabcdx"))
