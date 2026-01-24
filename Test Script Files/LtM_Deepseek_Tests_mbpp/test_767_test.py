import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertEqual(get_Pairs_Count([1, 1, 1, 1], 4, 2), 6)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 10), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(get_Pairs_Count([5], 1, 5), 0)

    def test_edge_case_sum_zero(self):
        self.assertEqual(get_Pairs_Count([1, -1, 0, 0], 4, 0), 3)

    def test_complex_case_duplicates(self):
        self.assertEqual(get_Pairs_Count([1, 2, 1, 2, 3, 4], 6, 3), 2)

    def test_complex_case_negative_numbers(self):
        self.assertEqual(get_Pairs_Count([-1, -2, 3, 4, 5], 5, 3), 1)
