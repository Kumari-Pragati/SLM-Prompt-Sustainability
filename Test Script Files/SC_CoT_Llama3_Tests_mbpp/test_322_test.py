import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(position_min([1]), [0])

    def test_edge_case_multiple_minima_list(self):
        self.assertEqual(position_min([1, 1, 2, 3, 4]), [0, 1])

    def test_edge_case_negative_numbers_list(self):
        self.assertEqual(position_min([-1, -2, -3, 4, 5]), [0, 1, 2])

    def test_edge_case_all_negative_numbers_list(self):
        self.assertEqual(position_min([-1, -2, -3, -4, -5]), [0, 1, 2, 3, 4])

    def test_edge_case_all_positive_numbers_list(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])

    def test_edge_case_all_equal_numbers_list(self):
        self.assertEqual(position_min([1, 1, 1, 1, 1]), [0, 1, 2, 3, 4])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(position_min([1, 2, 2, 3, 4, 4, 5]), [0, 1, 2, 3, 4, 5])

    def test_edge_case_list_with_duplicates_and_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -2, -3, -3, -4, -5]), [0, 1, 2, 3, 4, 5])

    def test_edge_case_list_with_duplicates_and_negative_numbers_and_positive_numbers(self):
        self.assertEqual(position_min([-1, -2, -2, -3, -3, -4, -5, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])
