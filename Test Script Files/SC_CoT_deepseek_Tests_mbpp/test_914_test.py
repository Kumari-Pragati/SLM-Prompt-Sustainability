import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Two_Alter('aabbaa'))

    def test_edge_case(self):
        self.assertFalse(is_Two_Alter('aaa'))

    def test_boundary_case(self):
        self.assertFalse(is_Two_Alter(''))
        self.assertTrue(is_Two_Alter('a'))
        self.assertTrue(is_Two_Alter('aa'))

    def test_corner_case(self):
        self.assertFalse(is_Two_Alter('ab'))
        self.assertFalse(is_Two_Alter('ba'))
        self.assertFalse(is_Two_Alter('abc'))
        self.assertFalse(is_Two_Alter('bca'))
        self.assertFalse(is_Two_Alter('cab'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Two_Alter(123)
        with self.assertRaises(TypeError):
            is_Two_Alter(None)
        with self.assertRaises(TypeError):
            is_Two_Alter([1, 2, 3])
