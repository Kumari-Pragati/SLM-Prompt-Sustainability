import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_typical_case(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        expected_result = [5, 7, 9]
        self.assertEqual(sum_list(lst1, lst2), expected_result)

    def test_empty_lists(self):
        lst1 = []
        lst2 = []
        expected_result = []
        self.assertEqual(sum_list(lst1, lst2), expected_result)

    def test_different_lengths(self):
        lst1 = [1, 2, 3, 4]
        lst2 = [4, 5]
        expected_result = [5, 7, 3]
        self.assertEqual(sum_list(lst1, lst2), expected_result)

    def test_negative_numbers(self):
        lst1 = [-1, -2, -3]
        lst2 = [-4, -5, -6]
        expected_result = [-5, -7, -9]
        self.assertEqual(sum_list(lst1, lst2), expected_result)

    def test_zeroes(self):
        lst1 = [0, 0, 0]
        lst2 = [0, 0, 0]
        expected_result = [0, 0, 0]
        self.assertEqual(sum_list(lst1, lst2), expected_result)
