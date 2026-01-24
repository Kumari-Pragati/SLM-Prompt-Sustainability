import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(is_Two_Alter("abcd"))
        self.assertTrue(is_Two_Alter("xyzw"))

    def test_edge_cases(self):
        self.assertTrue(is_Two_Alter("aaab"))
        self.assertTrue(is_Two_Alter("abcdx"))
        self.assertTrue(is_Two_Alter("abcd_"))
        self.assertTrue(is_Two_Alter("1234"))

    def test_boundary_cases(self):
        self.assertTrue(is_Two_Alter("a"))
        self.assertTrue(is_Two_Alter("ab"))
        self.assertTrue(is_Two_Alter("abc"))
        self.assertTrue(is_Two_Alter("abcdx"))
        self.assertTrue(is_Two_Alter("abcdxy"))

    def test_special_cases(self):
        self.assertFalse(is_Two_Alter("aaa"))
        self.assertFalse(is_Two_Alter("abab"))
        self.assertFalse(is_Two_Alter("abba"))
        self.assertFalse(is_Two_Alter("ababab"))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_Two_Alter, 123)
        self.assertRaises(TypeError, is_Two_Alter, [1, 2, 3, 4])
        self.assertRaises(TypeError, is_Two_Alter, (1, 2, 3, 4))
        self.assertRaises(TypeError, is_Two_Alter, set([1, 2, 3, 4]))
        self.assertRaises(TypeError, is_Two_Alter, frozenset([1, 2, 3, 4]))
        self.assertRaises(TypeError, is_Two_Alter, {"a": 1, "b": 2, "c": 3, "d": 4})
