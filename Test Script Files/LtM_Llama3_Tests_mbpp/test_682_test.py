import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_empty(self):
        self.assertEqual(mul_list([], []), [])

    def test_single(self):
        self.assertEqual(mul_list([1], [2]), [2])
        self.assertEqual(mul_list([1], []), [])

    def test_zero(self):
        self.assertEqual(mul_list([1, 2, 3], [0, 0, 0]), [0, 0, 0])
        self.assertEqual(mul_list([0, 0, 0], [1, 2, 3]), [0, 0, 0])

    def test_negative(self):
        self.assertEqual(mul_list([-1, -2, -3], [4, 5, 6]), [-4, -10, -18])
        self.assertEqual(mul_list([1, 2, 3], [-4, -5, -6]), [-4, -10, -18])

    def test_large(self):
        self.assertEqual(mul_list([1000, 2000, 3000], [4000, 5000, 6000]), [4000000, 10000000, 18000000])
