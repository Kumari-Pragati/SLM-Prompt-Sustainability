import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Two_Alter('aab'))
        self.assertTrue(is_Two_Alter('abcabc'))
        self.assertFalse(is_Two_Alter('abcabcabc'))

    def test_edge_cases(self):
        self.assertFalse(is_Two_Alter(''))
        self.assertFalse(is_Two_Alter('a'))
        self.assertFalse(is_Two_Alter('aa'))
        self.assertFalse(is_Two_Alter('aaa'))

    def test_corner_cases(self):
        self.assertTrue(is_Two_Alter('aabbaabb'))
        self.assertFalse(is_Two_Alter('aabbaabbaabb'))
        self.assertFalse(is_Two_Alter('aabb'))
        self.assertFalse(is_Two_Alter('aabbcc'))
