import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_multiple_elements_array(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 6)

    def test_array_with_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 3, 3], 6), 6)

    def test_array_with_duplicates_and_non_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 3, 3, 4, 5], 8), 9)

    def test_empty_array(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_array_with_no_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 5)
