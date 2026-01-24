import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_Two_Alter("abc"))
        self.assertTrue(is_Two_Alter("abcd"))
        self.assertTrue(is_Two_Alter("abcde"))

    def test_edge_cases(self):
        self.assertFalse(is_Two_Alter("aa"))
        self.assertFalse(is_Two_Alter("abab"))
        self.assertFalse(is_Two_Alter("abcba"))

    def test_invalid_inputs(self):
        self.assertFalse(is_Two_Alter(""))
        self.assertFalse(is_Two_Alter("a"))
        self.assertFalse(is_Two_Alter("aabb"))

    def test_corner_cases(self):
        self.assertTrue(is_Two_Alter("abcde"))
        self.assertTrue(is_Two_Alter("abcdeff"))
        self.assertTrue(is_Two_Alter("abcdefg"))
