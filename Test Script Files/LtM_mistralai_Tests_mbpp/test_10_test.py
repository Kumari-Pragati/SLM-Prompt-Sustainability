import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(small_nnum([1, 2, 3, 4, 5], 2), [1, 2])
        self.assertListEqual(small_nnum([10, 20, 30, 40, 50], 3), [10, 20, 30])

    def test_edge_cases(self):
        self.assertListEqual(small_nnum([], 2), [])
        self.assertListEqual(small_nnum([1], 1), [1])
        self.assertListEqual(small_nnum([1, 2, 3], 4), [1, 2, 3])
        self.assertListEqual(small_nnum([-1, -2, -3], 2), [-3, -2])

    def test_complex(self):
        self.assertListEqual(small_nnum([1, 2, 3, 2, 1], 2), [1, 2])
        self.assertListEqual(small_nnum([10, 20, 10, 30, 20], 3), [10, 20, 30])
