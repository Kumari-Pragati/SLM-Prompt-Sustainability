import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Two_Alter("abcdefg"))
        self.assertTrue(is_Two_Alter("xyz12345"))
        self.assertTrue(is_Two_Alter("ABCDEFG"))

    def test_edge_case_short(self):
        self.assertFalse(is_Two_Alter("a"))
        self.assertFalse(is_Two_Alter("ab"))
        self.assertFalse(is_Two_Alter("abc"))

    def test_edge_case_long(self):
        self.assertTrue(is_Two_Alter("abcdabcdefg"))
        self.assertTrue(is_Two_Alter("1234567890"))
        self.assertTrue(is_Two_Alter("ABCDEFGHIJKLM"))

    def test_corner_case_same_first_and_second(self):
        self.assertFalse(is_Two_Alter("aaa"))
        self.assertFalse(is_Two_Alter("111"))
        self.assertFalse(is_Two_Alter("AAA"))

    def test_corner_case_same_last_and_second_to_last(self):
        self.assertFalse(is_Two_Alter("abcdab"))
        self.assertFalse(is_Two_Alter("123412"))
        self.assertFalse(is_Two_Alter("ABCDEFAB"))
