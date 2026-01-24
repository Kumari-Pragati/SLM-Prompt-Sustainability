import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_simple_consecutive_different(self):
        self.assertTrue(is_Two_Alter("abc"))
        self.assertTrue(is_Two_Alter("def"))
        self.assertTrue(is_Two_Alter("ghi"))

    def test_simple_consecutive_same(self):
        self.assertFalse(is_Two_Alter("aaa"))
        self.assertFalse(is_Two_Alter("bbb"))
        self.assertFalse(is_Two_Alter("ccc"))

    def test_edge_single_char(self):
        self.assertFalse(is_Two_Alter("a"))
        self.assertFalse(is_Two_Alter(""))

    def test_edge_two_chars(self):
        self.assertTrue(is_Two_Alter("ab"))
        self.assertFalse(is_Two_Alter("aa"))

    def test_edge_last_two_chars(self):
        self.assertTrue(is_Two_Alter("abcdef"))
        self.assertFalse(is_Two_Alter("abcdg"))

    def test_edge_first_two_chars(self):
        self.assertTrue(is_Two_Alter("xyz"))
        self.assertFalse(is_Two_Alter("xyy"))
