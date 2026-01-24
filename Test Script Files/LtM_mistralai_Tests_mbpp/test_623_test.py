import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4], 2), [1, 4, 9, 16])
        self.assertListEqual(nth_nums([5, 10, 15, 20], 3), [125, 10000, 22500, 80000])

    def test_edge_and_boundary(self):
        self.assertListEqual(nth_nums([], 2), [])
        self.assertListEqual(nth_nums([0], 2), [0])
        self.assertListEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])
        self.assertListEqual(nth_nums([1, 2, 3], 0), [1, 2, 3])

    def test_complex(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4, 5], 3), [1, 8, 27, 64, 125])
        self.assertListEqual(nth_nums([10, 20, 30, 40], 5), [100000, 800000, 2700000, 16000000])
        self.assertListEqual(nth_nums([0.5, 1.5, 2.5], 2), [0.25, 3.375, 6.25])
