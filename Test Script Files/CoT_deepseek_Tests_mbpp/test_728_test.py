import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_typical_case(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        expected_output = [5, 7, 9]
        self.assertEqual(sum_list(lst1, lst2), expected_output)

    def test_empty_lists(self):
        lst1 = []
        lst2 = []
        expected_output = []
        self.assertEqual(sum_list(lst1, lst2), expected_output)

    def test_different_lengths(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5]
        with self.assertRaises(IndexError):
            sum_list(lst1, lst2)

    def test_negative_numbers(self):
        lst1 = [-1, -2, -3]
        lst2 = [-4, -5, -6]
        expected_output = [-5, -7, -9]
        self.assertEqual(sum_list(lst1, lst2), expected_output)

    def test_zeroes(self):
        lst1 = [0, 0, 0]
        lst2 = [0, 0, 0]
        expected_output = [0, 0, 0]
        self.assertEqual(sum_list(lst1, lst2), expected_output)
