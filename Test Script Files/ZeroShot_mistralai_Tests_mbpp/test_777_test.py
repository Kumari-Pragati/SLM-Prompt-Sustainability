import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_duplicate_elements_list(self):
        self.assertEqual(find_Sum([1, 1, 2], 3), 1)

    def test_unique_elements_list(self):
        self.assertEqual(find_Sum([1, 2, 3], 3), 6)

    def test_negative_numbers_list(self):
        self.assertEqual(find_Sum([-1, -2, -3], 3), -6)

    def test_mixed_numbers_list(self):
        self.assertEqual(find_Sum([1, -2, 3, -4, 5], 5), 10)
