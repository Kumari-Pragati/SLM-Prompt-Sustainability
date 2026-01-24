import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 9)

    def test_edge_case(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 0)

    def test_zero_array(self):
        arr = [0, 0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), -1)

    def test_single_element_array(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 1)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            max_sum(arr, n)
