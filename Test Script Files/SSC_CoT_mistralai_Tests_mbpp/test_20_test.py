import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(3))
        self.assertTrue(is_woodall(5))
        self.assertTrue(is_woodall(7))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))
        self.assertFalse(is_woodall(8))
        self.assertFalse(is_woodall(9))
        self.assertFalse(is_woodall(10))
        self.assertFalse(is_woodall(11))
        self.assertFalse(is_woodall(12))
        self.assertFalse(is_woodall(13))
        self.assertFalse(is_woodall(14))
        self.assertFalse(is_woodall(15))
        self.assertFalse(is_woodall(16))
        self.assertFalse(is_woodall(17))
        self.assertFalse(is_woodall(18))
        self.assertFalse(is_woodall(19))
        self.assertFalse(is_woodall(20))
        self.assertFalse(is_woodall(21))
        self.assertFalse(is_woodall(22))
        self.assertFalse(is_woodall(23))
        self.assertFalse(is_woodall(24))
        self.assertFalse(is_woodall(25))
        self.assertFalse(is_woodall(26))
        self.assertFalse(is_woodall(27))
        self.assertFalse(is_woodall(28))
        self.assertFalse(is_woodall(29))
        self.assertFalse(is_woodall(30))
