import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 15)

    def test_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 1)

    def test_two_elements(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 3)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), -6)

    def test_mixed_numbers(self):
        arr = [-1, 2, -3, 4, -5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 5)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 0)

    def test_large_array(self):
        arr = [i for i in range(1, 1001)]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), sum(arr))
