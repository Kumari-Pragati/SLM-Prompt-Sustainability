import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_single_element_array_with_zero(self):
        self.assertEqual(find_Sum([0], 1), 0)

    def test_array_with_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4, 4], 6), 6)

    def test_array_with_duplicates_and_zero(self):
        self.assertEqual(find_Sum([0, 0, 1, 2, 2, 3, 4, 4], 8), 4)

    def test_array_with_duplicates_and_zero_and_negative(self):
        self.assertEqual(find_Sum([-1, -1, 0, 0, 1, 2, 2, 3, 4, 4], 10), 4)

    def test_array_with_no_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_array_with_no_duplicates_and_zero(self):
        self.assertEqual(find_Sum([0, 1, 2, 3, 4, 5], 6), 15)

    def test_array_with_no_duplicates_and_zero_and_negative(self):
        self.assertEqual(find_Sum([-1, 0, 1, 2, 3, 4, 5], 7), 15)
