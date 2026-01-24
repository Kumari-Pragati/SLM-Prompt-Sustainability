import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_typical_case(self):
        list = [[4, 7, 9, 10], [2, 3, 6, 8], [1, 5]]
        self.assertEqual(find_minimum_range(list), (1, 5))

    def test_edge_case_single_list(self):
        list = [[1, 2, 3]]
        self.assertEqual(find_minimum_range(list), (1, 3))

    def test_boundary_case_empty_list(self):
        list = []
        self.assertEqual(find_minimum_range(list), None)

    def test_corner_case_duplicate_values(self):
        list = [[1, 2, 2], [2, 3, 4], [1, 2]]
        self.assertEqual(find_minimum_range(list), (1, 2))

    def test_corner_case_reverse_sorted_lists(self):
        list = [[10, 9, 8], [7, 6, 5], [4, 3, 2]]
        self.assertEqual(find_minimum_range(list), (2, 10))

    def test_corner_case_same_values(self):
        list = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(find_minimum_range(list), (1, 1))
