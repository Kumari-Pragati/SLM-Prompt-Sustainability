import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_minimum_range([]))

    def test_single_element_list(self):
        result = find_minimum_range([[1]])
        self.assertEqual(result, (1, 1))

    def test_multiple_elements_same_value(self):
        result = find_minimum_range([[1, 1], [1, 1]])
        self.assertEqual(result, (1, 1))

    def test_multiple_elements_different_values(self):
        result = find_minimum_range([[1, 2], [3, 4]])
        self.assertEqual(result, (1, 3))

    def test_edge_case_single_list_with_min_and_max(self):
        result = find_minimum_range([[1, 2], [2, 3], [3, 4]])
        self.assertEqual(result, (1, 3))

    def test_edge_case_single_list_with_min_only(self):
        result = find_minimum_range([[1, 2], [2, 2], [3, 2]])
        self.assertEqual(result, (1, 2))

    def test_edge_case_single_list_with_max_only(self):
        result = find_minimum_range([[1, 2], [1, 3], [1, 4]])
        self.assertEqual(result, (1, 4))

    def test_edge_case_multiple_lists_with_min_and_max(self):
        result = find_minimum_range([[1, 2], [2, 3], [3, 4], [4, 5]])
        self.assertEqual(result, (1, 4))

    def test_edge_case_multiple_lists_with_min_only(self):
        result = find_minimum_range([[1, 2], [2, 2], [3, 2], [4, 2]])
        self.assertEqual(result, (1, 2))

    def test_edge_case_multiple_lists_with_max_only(self):
        result = find_minimum_range([[1, 2], [1, 3], [1, 4], [1, 5]])
        self.assertEqual(result, (1, 5))
