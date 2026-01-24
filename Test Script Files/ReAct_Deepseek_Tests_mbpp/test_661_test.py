import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_typical_case(self):
        arr = [3, 6, 9, 12, 15]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 33)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 5)

    def test_two_elements(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 3)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-3, -6, -9, -12, -15]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), -3)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 12000)

    def test_large_negative_numbers(self):
        arr = [-1000, -2000, -3000, -4000, -5000]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), -1000)

    def test_mixed_numbers(self):
        arr = [-1, 2, -3, 4, -5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 5)
