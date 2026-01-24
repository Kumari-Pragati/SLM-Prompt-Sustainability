import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_typical_input(self):
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertListEqual(larg_nnum([-1, -2, -3, -4, -5], 3), [-5, -4, -3])
        self.assertListEqual(larg_nnum([1, 2, 3], 3), [3, 2, 1])
        self.assertListEqual(larg_nnum([-1, -2, -3], 3), [-3, -2, -1])

    def test_edge_input(self):
        self.assertListEqual(larg_nnum([1, 2, 3], 1), [3])
        self.assertListEqual(larg_nnum([-1, -2, -3], 1), [-3])
        self.assertListEqual(larg_nnum([1, 2, 3], 0), [])
        self.assertListEqual(larg_nnum([-1, -2, -3], 0), [])

    def test_empty_input(self):
        self.assertRaises(TypeError, larg_nnum, [], 3)
        self.assertRaises(TypeError, larg_nnum, (1, 2, 3, 4), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, larg_nnum, 'str', 3)
        self.assertRaises(TypeError, larg_nnum, [1, 2, 'three'], 3)
