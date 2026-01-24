import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_minimum_range([]), (float('-inf'), float('inf')))

    def test_single_element_list(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_multiple_elements_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5, 6]]), (1, 6))

    def test_list_with_duplicates(self):
        self.assertEqual(find_minimum_range([[1, 1, 2], [3, 4, 5]]), (1, 5))

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_minimum_range([[-1, -2, -3], [4, 5, 6]]), (-3, 6))

    def test_list_with_negative_and_positive_numbers(self):
        self.assertEqual(find_minimum_range([[-1, -2, 3], [4, 5, 6]]), (-2, 6))

    def test_list_with_negative_numbers_and_duplicates(self):
        self.assertEqual(find_minimum_range([[-1, -1, -2], [3, 4, 5]]), (-2, 5))
