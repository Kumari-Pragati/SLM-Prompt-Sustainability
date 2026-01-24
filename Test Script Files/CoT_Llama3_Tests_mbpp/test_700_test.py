import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_edge_case_min_equal_to_min(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_edge_case_max_equal_to_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 4, 4), 1)

    def test_edge_case_min_greater_than_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 5, 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_range_in_list([3], 1, 5), 1)

    def test_edge_case_single_element_list_out_of_range(self):
        self.assertEqual(count_range_in_list([6], 1, 5), 0)

    def test_edge_case_single_element_list_equal_to_min(self):
        self.assertEqual(count_range_in_list([2], 2, 5), 1)

    def test_edge_case_single_element_list_equal_to_max(self):
        self.assertEqual(count_range_in_list([4], 1, 4), 1)

    def test_edge_case_single_element_list_equal_to_min_and_max(self):
        self.assertEqual(count_range_in_list([2], 2, 2), 1)

    def test_invalid_input_non_integer_min(self):
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3, 4, 5], 'a', 4)

    def test_invalid_input_non_integer_max(self):
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3, 4, 5], 1, 'a')

    def test_invalid_input_non_integer_min_and_max(self):
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3, 4, 5], 'a', 'b')
