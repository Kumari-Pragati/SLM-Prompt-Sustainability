import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        expected_sum = 0
        for i in range(n - 1, -1, -1):
            expected_sum += i * arr[i] - (n - 1 - i) * arr[i]
        self.assertEqual(sum_Pairs(arr, n), expected_sum)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_single_element_array(self):
        arr = [5]
        n = 1
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        expected_sum = 0
        for i in range(n - 1, -1, -1):
            expected_sum += i * arr[i] - (n - 1 - i) * arr[i]
        self.assertEqual(sum_Pairs(arr, n), expected_sum)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        n = len(arr)
        expected_sum = 0
        for i in range(n - 1, -1, -1):
            expected_sum += i * arr[i] - (n - 1 - i) * arr[i]
        self.assertEqual(sum_Pairs(arr, n), expected_sum)

    def test_large_array(self):
        arr = list(range(1, 1001))
        n = len(arr)
        expected_sum = 0
        for i in range(n - 1, -1, -1):
            expected_sum += i * arr[i] - (n - 1 - i) * arr[i]
        self.assertEqual(sum_Pairs(arr, n), expected_sum)
