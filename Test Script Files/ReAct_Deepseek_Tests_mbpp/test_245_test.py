import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 2)

    def test_edge_case_with_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), -1)

    def test_edge_case_with_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 5)

    def test_edge_case_with_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 0)

    def test_typical_case_with_duplicates(self):
        arr = [1, 2, 3, 4, 5, 5]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 10)

    def test_edge_case_with_maximum_and_minimum_values(self):
        arr = [float('-inf'), float('inf')]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 0)

    def test_typical_case_with_large_numbers(self):
        arr = [1000, 2000, 3000, 4000]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 10000)
