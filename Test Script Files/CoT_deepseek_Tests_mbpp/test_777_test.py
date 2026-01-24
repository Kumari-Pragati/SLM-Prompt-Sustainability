import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_single_element(self):
        self.assertEqual(find_Sum([5], 1), 5)

    def test_duplicate_elements(self):
        self.assertEqual(find_Sum([2, 2, 2, 2], 4), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4, -5], 5), -6)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            find_Sum([], 0)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            find_Sum([1, 2, '3', 4, 5], 5)

    def test_large_numbers(self):
        self.assertEqual(find_Sum([10**6, 2*10**6, 3*10**6, 4*10**6, 5*10**6], 5), 15*10**6)

    def test_sorted_array(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_unsorted_array(self):
        self.assertEqual(find_Sum([5, 1, 2, 4, 3], 5), 15)
