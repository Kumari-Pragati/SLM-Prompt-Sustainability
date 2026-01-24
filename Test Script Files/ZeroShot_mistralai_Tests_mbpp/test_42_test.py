import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_single_element_list_with_duplicate(self):
        self.assertEqual(find_Sum([1, 1], 2), 1)

    def test_list_with_duplicate_element(self):
        self.assertEqual(find_Sum([1, 2, 1, 3, 2], 5), 2)

    def test_list_with_multiple_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 1, 1, 3, 2, 2], 7), 2)

    def test_list_with_only_duplicates(self):
        self.assertEqual(find_Sum([1, 1, 1, 1], 4), 1)
