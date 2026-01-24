import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 2), [4, 5])
        self.assertListEqual(larg_nnum([10, 20, 30, 40, 50], 3), [50, 40, 30])

    def test_edge_cases(self):
        self.assertListEqual(larg_nnum([], 2), [])
        self.assertListEqual(larg_nnum([1], 1), [1])
        self.assertListEqual(larg_nnum([1, 2, 3], 4), [1, 2, 3])
        self.assertListEqual(larg_nnum([1, 2, 3], 0), [])
        self.assertListEqual(larg_nnum([1, 2, 3], 5), [1, 2, 3])

    def test_complex(self):
        self.assertListEqual(larg_nnum([1, 2, 2, 3, 2, 3, 4, 2, 3], 3), [4, 3, 3])
        self.assertListEqual(larg_nnum([-1, -2, -3, -4, -5], 2), [-5, -4])
        self.assertListEqual(larg_nnum([1000000000, 1, 2, 3, 4, 5], 3), [1000000000, 4, 3])
