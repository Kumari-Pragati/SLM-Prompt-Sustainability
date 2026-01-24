import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_Two_Alter("abcabc"))

    def test_false(self):
        self.assertFalse(is_Two_Alter("abab"))

    def test_edge_case1(self):
        self.assertTrue(is_Two_Alter("a"))

    def test_edge_case2(self):
        self.assertTrue(is_Two_Alter("aa"))

    def test_edge_case3(self):
        self.assertFalse(is_Two_Alter("aabb"))

    def test_edge_case4(self):
        self.assertFalse(is_Two_Alter("ababab"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Two_Alter(None)
