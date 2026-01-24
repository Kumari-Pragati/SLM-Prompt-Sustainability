import unittest
from656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_find_min_sum_empty_lists(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)

    def test_find_min_sum_single_element(self):
        self.assertEqual(find_Min_Sum([1], [1], 1), 0)
        self.assertEqual(find_Min_Sum([1], [2], 1), 1)

    def test_find_min_sum_different_lengths(self):
        self.assertEqual(find_Min_Sum([1, 2], [1, 2, 3], 2), 1)
        self.assertEqual(find_Min_Sum([1, 2], [1, 2, 3, 4], 3), 2)

    def test_find_min_sum_different_numbers(self):
        self.assertEqual(find_Min_Sum([1, 2], [3, 4], 2), 3)
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 6)

    def test_find_min_sum_same_numbers(self):
        self.assertEqual(find_Min_Sum([1, 1], [1, 1], 2), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 3), 0)
