import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_list(self):
        for element in [1, 2, 3]:
            self.assertEqual(find_Sum([element], 1), 0)

    def test_single_repeated_element_list(self):
        self.assertEqual(find_Sum([1, 1], 2), 1)

    def test_multiple_repeated_elements_list(self):
        self.assertEqual(find_Sum([1, 1, 2, 2, 3, 3], 6), 6)

    def test_list_with_no_repeated_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -1, 0, 1, 1], 5), -1)

    def test_list_with_zero(self):
        self.assertEqual(find_Sum([0, 0, 1, 1], 4), 0)

    def test_list_with_large_numbers(self):
        self.assertEqual(find_Sum([1000, 1000, 1001], 3), 1000)

    def test_list_with_small_numbers(self):
        self.assertEqual(find_Sum([1, 1, -1], 3), 1)

    def test_list_with_duplicate_first_element(self):
        self.assertEqual(find_Sum([1, 1, 2], 3), 1)

    def test_list_with_duplicate_last_element(self):
        self.assertEqual(find_Sum([1, 2, 2], 3), 2)

    def test_list_with_duplicate_middle_element(self):
        self.assertEqual(find_Sum([1, 2, 2, 3], 3), 2)

    def test_list_with_long_sequence(self):
        self.assertEqual(find_Sum([1] * 1000 + [2] * 1000 + [3] * 1000, 3000), 1000)

    def test_list_with_negative_numbers_and_zero(self):
        self.assertEqual(find_Sum([-1, 0, -1], 3), -1)

    def test_list_with_large_and_small_numbers(self):
        self.assertEqual(find_Sum([10000, 1, 10000], 3), 10000)
