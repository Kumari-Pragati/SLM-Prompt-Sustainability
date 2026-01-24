import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 10), 0)

    def test_single_element_list(self):
        self.assertEqual(count_range_in_list([5], 1, 10), 1)

    def test_list_with_no_elements_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 11, 12], 5, 10), 0)

    def test_list_with_elements_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10), 10)

    def test_list_with_elements_at_min_max(self):
        self.assertEqual(count_range_in_list([1, 10], 1, 10), 2)

    def test_list_with_elements_at_min_max_and_in_range(self):
        self.assertEqual(count_range_in_list([1, 5, 10], 1, 10), 3)

    def test_list_with_elements_at_min_max_and_out_of_range(self):
        self.assertEqual(count_range_in_list([1, 10, 15], 1, 10), 2)

    def test_list_with_elements_at_min_max_and_out_of_range_and_in_range(self):
        self.assertEqual(count_range_in_list([1, 5, 10, 15], 1, 10), 3)
