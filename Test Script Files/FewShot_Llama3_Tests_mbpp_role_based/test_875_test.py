import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 3), (2, 4), (5, 7)]
        self.assertEqual(min_difference(test_list), 1)

    def test_edge_case_single_element(self):
        test_list = [(1, 1)]
        self.assertEqual(min_difference(test_list), 0)

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(min_difference(test_list), None)

    def test_edge_case_single_element_list(self):
        test_list = [(1,)]
        with self.assertRaises(IndexError):
            min_difference(test_list)

    def test_edge_case_list_with_duplicates(self):
        test_list = [(1, 1), (2, 2), (3, 3)]
        self.assertEqual(min_difference(test_list), 0)

    def test_edge_case_list_with_negative_numbers(self):
        test_list = [(-1, -3), (-2, -4), (-5, -7)]
        self.assertEqual(min_difference(test_list), 1)

    def test_edge_case_list_with_zero(self):
        test_list = [(0, 0), (1, 1), (2, 2)]
        self.assertEqual(min_difference(test_list), 0)
