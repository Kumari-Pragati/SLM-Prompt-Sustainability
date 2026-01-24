import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case(self):
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_zero_array(self):
        self.assertEqual(max_sum([0, 0, 0, 0, 0], 5), 0)

    def test_single_element_array(self):
        self.assertEqual(max_sum([5], 1), 5)

    def test_empty_array(self):
        self.assertEqual(max_sum([], 0), float('-Inf'))

    def test_negative_numbers(self):
        self.assertEqual(max_sum([-5, -2, 3, 4, -1], 4), 1)

    def test_all_negative_numbers(self):
        self.assertEqual(max_sum([-5, -2, -3, -4, -5], 5), float('-Inf'))
