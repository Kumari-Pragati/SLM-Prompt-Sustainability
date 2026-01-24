import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Two_Alter('aabbaabb'))
        self.assertTrue(is_Two_Alter('abcabcabc'))
        self.assertTrue(is_Two_Alter('123123123'))

    def test_edge_cases(self):
        self.assertFalse(is_Two_Alter(''))
        self.assertFalse(is_Two_Alter('a'))
        self.assertFalse(is_Two_Alter('aa'))
        self.assertFalse(is_Two_Alter('aaa'))
        self.assertFalse(is_Two_Alter('aab'))

    def test_boundary_conditions(self):
        self.assertFalse(is_Two_Alter('aabbaab'))
        self.assertFalse(is_Two_Alter('aabbaabb'))
        self.assertFalse(is_Two_Alter('aabbaabba'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Two_Alter(123)
        with self.assertRaises(TypeError):
            is_Two_Alter(None)
        with self.assertRaises(TypeError):
            is_Two_Alter(['a', 'b', 'c'])
