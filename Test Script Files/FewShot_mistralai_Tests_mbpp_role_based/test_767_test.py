import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 6), 2)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 7), 0)

    def test_empty_list(self):
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)
        self.assertEqual(get_Pairs_Count([1], 1, 2), 0)

    def test_negative_numbers(self):
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, 5), 1)
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, 0), 0)

    def test_duplicates(self):
        self.assertEqual(get_Pairs_Count([1, 1, 2, 3], 4, 2), 1)
        self.assertEqual(get_Pairs_Count([1, 1, 2, 3], 4, 4), 2)

    def test_sum_greater_than_array_sum(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3], 3, 4), 0)

    def test_sum_less_than_array_min(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3], 3, -1), 0)
