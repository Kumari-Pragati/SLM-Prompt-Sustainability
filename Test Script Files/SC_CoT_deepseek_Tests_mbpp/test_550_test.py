import unittest

from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Max([5], 0, 0), 5)

    def test_edge_case_two_elements(self):
        self.assertEqual(find_Max([5, 6], 0, 1), 6)

    def test_edge_case_descending_order(self):
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)

    def test_invalid_input_low_greater_than_high(self):
        with self.assertRaises(Exception):
            find_Max([1, 2, 3, 4, 5], 5, 4)

    def test_invalid_input_low_or_high_out_of_bounds(self):
        with self.assertRaises(Exception):
            find_Max([1, 2, 3, 4, 5], 6, 7)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(Exception):
            find_Max([], 0, 0)
