import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 1), 0)

    def test_single_element(self):
        self.assertEqual(count_range_in_list([5], 4, 6), 1)

    def test_multiple_elements_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 4)

    def test_multiple_elements_out_of_range(self):
        self.assertEqual(count_range_in_list([-1, 0, 1, 2, 3], -2, 6), 0)

    def test_min_equal_to_max(self):
        self.assertEqual(count_range_in_list([1, 1, 2, 3], 1, 1), 2)

    def test_min_greater_than_max(self):
        with self.assertRaises(ValueError):
            count_range_in_list([1, 2, 3], 4, 1)

    def test_min_less_than_first_element(self):
        with self.assertRaises(ValueError):
            count_range_in_list([-1, 0, 1, 2, 3], -2, -1)

    def test_max_greater_than_last_element(self):
        with self.assertRaises(ValueError):
            count_range_in_list([-1, 0, 1, 2, 3], 4, 4)
