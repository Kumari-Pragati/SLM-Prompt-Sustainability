import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), 15)
        self.assertEqual(max_sum([1, -2, 3, -4, 5], 5), 13)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum([1], 1), 1)
        self.assertEqual(max_sum([-1], 1), -1)

    def test_edge_case_single_pair(self):
        self.assertEqual(max_sum([1, 2], 2), 3)
        self.assertEqual(max_sum([-1, -2], 2), -1)

    def test_corner_case_all_negative(self):
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), 15)

    def test_corner_case_all_positive(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 15)

    def test_corner_case_all_zero(self):
        self.assertEqual(max_sum([0, 0, 0, 0, 0], 5), 0)
