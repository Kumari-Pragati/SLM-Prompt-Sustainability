import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 2), [[1, 3, 5], [2, 4]])

    def test_edge_condition_empty_list(self):
        self.assertEqual(list_split([], 2), [[]])

    def test_edge_condition_step_equals_one(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 1), [[1], [2], [3], [4], [5]])

    def test_edge_condition_step_greater_than_list_length(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 6), [[1, 2, 3, 4, 5]])

    def test_boundary_condition_step_equals_zero(self):
        with self.assertRaises(ValueError):
            list_split([1, 2, 3, 4, 5], 0)

    def test_complex_case_step_equals_two_with_duplicates(self):
        self.assertEqual(list_split([1, 1, 2, 2, 3, 3], 2), [[1, 2, 3], [1, 2, 3]])

    def test_complex_case_step_greater_than_two(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [[1, 4, 7], [2, 5, 8], [3, 6, 9], [10]])
