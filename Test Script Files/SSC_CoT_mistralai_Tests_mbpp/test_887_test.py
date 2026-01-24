import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))

    def test_edge_input(self):
        self.assertTrue(is_odd(0))  # 0^1 == 0-1 = -1, which is False
        self.assertFalse(is_odd(-1))  # -1^1 == -1+1 = 0, which is False
        self.assertFalse(is_odd(2))  # 2^1 == 2-1 = 1, which is True

    def test_boundary_input(self):
        self.assertTrue(is_odd(2147483647))  # max int
        self.assertTrue(is_odd(-2147483648))  # min int

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_odd, 3.14)  # floating point number
        self.assertRaises(TypeError, is_odd, ['str'])  # string
        self.assertRaises(TypeError, is_odd, (1, 2, 3))  # tuple
        self.assertRaises(TypeError, is_odd, set([1, 2, 3]))  # set
