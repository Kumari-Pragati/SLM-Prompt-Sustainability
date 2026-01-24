import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Two_Alter('aabbcc'))
        self.assertTrue(is_Two_Alter('123456'))
        self.assertTrue(is_Two_Alter('abcabcabc'))

    def test_edge_cases(self):
        self.assertFalse(is_Two_Alter('aab'))
        self.assertFalse(is_Two_Alter('121'))
        self.assertFalse(is_Two_Alter('abc'))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            is_Two_Alter(12345)
        with self.assertRaises(TypeError):
            is_Two_Alter(['a', 'b', 'c'])
