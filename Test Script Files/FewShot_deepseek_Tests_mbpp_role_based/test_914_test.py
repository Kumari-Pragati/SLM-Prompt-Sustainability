import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Two_Alter('aabbaa'))

    def test_edge_case(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_boundary_case(self):
        self.assertFalse(is_Two_Alter('aa'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Two_Alter(12345)
