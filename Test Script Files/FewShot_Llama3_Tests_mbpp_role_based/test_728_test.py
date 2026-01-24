import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_sum_list_with_positive_numbers(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        result = sum_list(lst1, lst2)
        self.assertEqual(result, [5, 7, 9])

    def test_sum_list_with_negative_numbers(self):
        lst1 = [-1, -2, -3]
        lst2 = [-4, -5, -6]
        result = sum_list(lst1, lst2)
        self.assertEqual(result, [-5, -7, -9])

    def test_sum_list_with_mixed_numbers(self):
        lst1 = [1, -2, 3]
        lst2 = [4, -5, 6]
        result = sum_list(lst1, lst2)
        self.assertEqual(result, [5, -7, 9])

    def test_sum_list_with_lists_of_different_lengths(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5]
        result = sum_list(lst1, lst2)
        self.assertEqual(result, [5, 7])

    def test_sum_list_with_empty_lists(self):
        lst1 = []
        lst2 = []
        result = sum_list(lst1, lst2)
        self.assertEqual(result, [])
