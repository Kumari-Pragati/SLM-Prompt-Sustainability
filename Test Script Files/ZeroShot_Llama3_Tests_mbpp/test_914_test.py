import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_is_Two_Alter_true(self):
        self.assertTrue(is_Two_Alter("abcde"))
        self.assertTrue(is_Two_Alter("aabbcc"))
        self.assertTrue(is_Two_Alter("123456"))

    def test_is_Two_Alter_false(self):
        self.assertFalse(is_Two_Alter("abab"))
        self.assertFalse(is_Two_Alter("abcabc"))
        self.assertFalse(is_Two_Alter("aabb"))

    def test_is_Two_Alter_edge_cases(self):
        self.assertTrue(is_Two_Alter("a"))
        self.assertTrue(is_Two_Alter("ab"))
        self.assertTrue(is_Two_Alter("abc"))

    def test_is_Two_Alter_empty_string(self):
        with self.assertRaises(TypeError):
            is_Two_Alter("")
