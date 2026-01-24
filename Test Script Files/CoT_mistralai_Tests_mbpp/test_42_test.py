import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_find_sum_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_find_sum_single_element(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_find_sum_single_duplicate(self):
        self.assertEqual(find_Sum([1, 1], 2), 1)

    def test_find_sum_multiple_duplicates(self):
        self.assertEqual(find_Sum([1, 1, 2, 1, 2], 5), 4)

    def test_find_sum_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -1, 0, 1], 4), -1)

    def test_find_sum_large_numbers(self):
        self.assertEqual(find_Sum([100, 100, 200, 100], 4), 100)

    def test_find_sum_no_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 3, 4], 4), 0)

    def test_find_sum_invalid_input_list(self):
        self.assertRaises(TypeError, find_Sum, [1, 2, 3], 'invalid')

    def test_find_sum_invalid_input_count(self):
        self.assertRaises(TypeError, find_Sum, [1, 2, 3], -1)
