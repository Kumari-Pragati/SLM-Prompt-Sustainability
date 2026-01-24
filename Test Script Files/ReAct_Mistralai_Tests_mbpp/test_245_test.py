import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum([]), 0)

    def test_single_element(self):
        for num in range(1, 101):
            self.assertEqual(max_sum([num]), num)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_sum(arr), 15)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_sum(arr), 15)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        self.assertEqual(max_sum(arr), 13)

    def test_zero(self):
        arr = [0, 1, 2, 3, 4]
        self.assertEqual(max_sum(arr), 10)

    def test_large_numbers(self):
        arr = [1000000, 2000000, 3000000, 4000000, 5000000]
        self.assertEqual(max_sum(arr), 15000000)

    def test_negative_large_numbers(self):
        arr = [-1000000, -2000000, -3000000, -4000000, -5000000]
        self.assertEqual(max_sum(arr), 15000000)

    def test_mixed_large_numbers(self):
        arr = [1000000, -2000000, 3000000, -4000000, 5000000]
        self.assertEqual(max_sum(arr), 14000000)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum([1]), 1)
        self.assertEqual(max_sum([-1]), -1)

    def test_edge_case_two_elements(self):
        self.assertEqual(max_sum([1, 2]), 3)
        self.assertEqual(max_sum([-1, -2]), -1)

    def test_edge_case_negative_sum(self):
        arr = [-1, -2, -3]
        self.assertEqual(max_sum(arr), 0)

    def test_edge_case_zero_sum(self):
        arr = [0, 0, 0]
        self.assertEqual(max_sum(arr), 0)
