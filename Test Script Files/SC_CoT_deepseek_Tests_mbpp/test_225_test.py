import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min([4, 5, 6, 7, 8, 9, 1, 2, 3], 0, 8), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min([1], 0, 0), 1)

    def test_edge_case_sorted_descending(self):
        self.assertEqual(find_Min([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8), 1)

    def test_edge_case_sorted_ascending(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8), 1)

    def test_corner_case_duplicates(self):
        self.assertEqual(find_Min([1, 3, 3, 5, 5, 5, 7, 7, 7, 9], 0, 9), 1)

    def test_invalid_input_low_greater_than_high(self):
        with self.assertRaises(Exception):
            find_Min([4, 5, 6, 7, 8, 9, 1, 2, 3], 10, 5)

    def test_invalid_input_low_negative(self):
        with self.assertRaises(Exception):
            find_Min([4, 5, 6, 7, 8, 9, 1, 2, 3], -1, 8)

    def test_invalid_input_high_greater_than_length(self):
        with self.assertRaises(Exception):
            find_Min([4, 5, 6, 7, 8, 9, 1, 2, 3], 0, 10)
