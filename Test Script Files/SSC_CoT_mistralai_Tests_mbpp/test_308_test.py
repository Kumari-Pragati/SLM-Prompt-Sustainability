import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 15, 18])
        self.assertListEqual(large_product([10, 20, 30], [4, 50, 60], 2), [200, 300])

    def test_edge_and_boundary(self):
        self.assertListEqual(large_product([], [], 1), [])
        self.assertListEqual(large_product([1], [], 1), [1])
        self.assertListEqual(large_product([1], [2], 0), [])
        self.assertListEqual(large_product([1], [2], 1), [2])
        self.assertListEqual(large_product([1], [2], 2), [2, 1])
        self.assertListEqual(large_product([1], [2], 3), [2, 1, 2])
        self.assertListEqual(large_product([1], [2, 3], 2), [6, 3])
        self.assertListEqual(large_product([1, 2], [3, 4], 2), [12, 8])

    def test_special_cases(self):
        self.assertListEqual(large_product([1, 1], [2], 1), [2])
        self.assertListEqual(large_product([1, 2], [2, 1], 1), [2])
        self.assertListEqual(large_product([1, 2], [2, 1], 2), [2, 1])
        self.assertListEqual(large_product([1, 2], [2, 1], 3), [2, 1, 2])
