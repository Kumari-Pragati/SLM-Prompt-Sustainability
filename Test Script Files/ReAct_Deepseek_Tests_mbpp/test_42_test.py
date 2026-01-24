import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_all_same_elements(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 5)

    def test_no_duplicate_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -2, -1], 5), -4)

    def test_large_numbers(self):
        self.assertEqual(find_Sum([1000, 2000, 3000, 2000, 1000], 5), 6000)

    def test_duplicate_numbers_with_zero(self):
        self.assertEqual(find_Sum([0, 0], 2), 0)

    def test_duplicate_numbers_with_float(self):
        self.assertEqual(find_Sum([1.5, 1.5], 2), 3.0)
