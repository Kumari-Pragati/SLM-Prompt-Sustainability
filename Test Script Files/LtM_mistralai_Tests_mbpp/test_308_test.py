import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 15, 18])
        self.assertListEqual(large_product([7, 8, 9], [10, 11, 12], 3), [70, 78, 86])

    def test_edge_cases(self):
        self.assertListEqual(large_product([], [], 0), [])
        self.assertListEqual(large_product([1], [], 0), [])
        self.assertListEqual(large_product([], [2], 0), [])
        self.assertListEqual(large_product([1], [], 1), [1])
        self.assertListEqual(large_product([], [2], 1), [2])
        self.assertListEqual(large_product([1], [2], 2), [2, 1])
        self.assertListEqual(large_product([1, 2], [], 0), [])
        self.assertListEqual(large_product([], [1, 2], 0), [])
        self.assertListEqual(large_product([1, 2], [], 1), [1])
        self.assertListEqual(large_product([], [1, 2], 1), [2])
        self.assertListEqual(large_product([1, 2], [3, 4], 0), [])
        self.assertListEqual(large_product([1, 2], [3, 4], 1), [6])
        self.assertListEqual(large_product([1, 2], [3, 4], 2), [6, 2])
        self.assertListEqual(large_product([1, 2], [3, 4], 3), [6, 2, 1])

    def test_complex(self):
        self.assertListEqual(large_product([1, 2], [3, 4, 5], 2), [12, 15])
        self.assertListEqual(large_product([1, 2], [3, 4, 5], 3), [12, 15, 6])
        self.assertListEqual(large_product([1, 2], [3, 4, 5], 4), [12, 15, 6, 1])
        self.assertListEqual(large_product([1, 2], [3, 4, 5], 5), [12, 15, 6, 1, 3])
