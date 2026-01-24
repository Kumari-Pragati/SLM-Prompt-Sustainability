import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_typical_use_case(self):
        list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertEqual(find_minimum_range(list), (1, 10))

    def test_edge_case_empty_list(self):
        list = []
        with self.assertRaises(IndexError):
            find_minimum_range(list)

    def test_edge_case_single_element_list(self):
        list = [[1]]
        self.assertEqual(find_minimum_range(list), (1, 1))

    def test_edge_case_single_element_list_with_duplicates(self):
        list = [[1, 1, 1, 1, 1]]
        self.assertEqual(find_minimum_range(list), (1, 1))

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers(self):
        list = [[-1, -1, -1, -1, -1]]
        self.assertEqual(find_minimum_range(list), (-1, -1))

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zero(self):
        list = [[-1, 0, -1, 0, -1]]
        self.assertEqual(find_minimum_range(list), (-1, 0))

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zero_and_negative_numbers(self):
        list = [[-1, 0, -1, 0, -1, -1]]
        self.assertEqual(find_minimum_range(list), (-1, -1))
