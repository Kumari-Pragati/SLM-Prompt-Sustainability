import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_Two_Alter('aab'))
        self.assertTrue(is_Two_Alter('abcabcabc'))
        self.assertTrue(is_Two_Alter('123123123'))

    def test_edge_conditions(self):
        self.assertFalse(is_Two_Alter(''))
        self.assertFalse(is_Two_Alter('a'))
        self.assertFalse(is_Two_Alter('aa'))
        self.assertFalse(is_Two_Alter('aaa'))
        self.assertFalse(is_Two_Alter('ab'))
        self.assertFalse(is_Two_Alter('aba'))

    def test_complex_cases(self):
        self.assertFalse(is_Two_Alter('abcabcabd'))
        self.assertFalse(is_Two_Alter('123123124'))
        self.assertFalse(is_Two_Alter('aabbaabbaab'))
        self.assertFalse(is_Two_Alter('aabbcc'))
