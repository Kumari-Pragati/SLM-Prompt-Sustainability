import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 7), 2)

    def test_edge_case_sum_in_array(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 5), 2)

    def test_edge_case_sum_out_of_array(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 10), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 1), 0)

    def test_edge_case_single_element_array_sum_in_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 1), 1)

    def test_edge_case_single_element_array_sum_out_of_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 2), 0)
