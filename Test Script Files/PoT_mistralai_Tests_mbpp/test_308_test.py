import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 15, 18])
        self.assertListEqual(large_product([10, 20, 30], [40, 50, 60], 2), [6000, 5030])

    def test_edge_case_short_nums(self):
        self.assertListEqual(large_product([1], [2], 1), [2])
        self.assertListEqual(large_product([1, 2], [], 1), [])
        self.assertListEqual(large_product([], [1, 2], 1), [])

    def test_edge_case_long_nums(self):
        self.assertListEqual(large_product([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5), [120, 150, 180, 210, 240])
        self.assertListEqual(large_product([10, 20, 30, 40, 50], [60, 70, 80, 90, 100], 6), [60000, 54000, 48000, 42000, 36000, 30000])

    def test_corner_case_empty_nums(self):
        self.assertListEqual(large_product([], [], 1), [])
