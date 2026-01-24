import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 8)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum([5], 1), 5)

    def test_boundary_case_empty_array(self):
        self.assertEqual(max_sum([], 0), float("-Inf"))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_sum([-1, -2, -3, -4], 4), -1)

    def test_corner_case_duplicate_numbers(self):
        self.assertEqual(max_sum([5, 5, 5, 5], 4), 20)

    def test_corner_case_large_numbers(self):
        self.assertEqual(max_sum([1000, 2000, 3000, 4000], 4), 10000)

    def test_corner_case_large_and_small_numbers(self):
        self.assertEqual(max_sum([-1000, 2000, -3000, 4000], 4), 3000)

    def test_corner_case_large_and_duplicate_numbers(self):
        self.assertEqual(max_sum([1000, 1000, 1000, 1000], 4), 4000)
