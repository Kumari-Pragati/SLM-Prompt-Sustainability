import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_consecutive_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 10)

    def test_duplicate_elements(self):
        self.assertEqual(find_Sum([1, 1, 2, 3, 4], 5), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4], 4), -10)

    def test_mixed_numbers(self):
        self.assertEqual(find_Sum([1, -2, 3, -4, 5], 5), 9)

    def test_large_numbers(self):
        self.assertEqual(find_Sum([1000000, 2000000, 3000000], 3), 5000000)

    def test_sorting_function(self):
        arr = [5, 3, 1, 4, 2]
        find_Sum(arr, len(arr))
        self.assertEqual(arr, sorted(arr))
