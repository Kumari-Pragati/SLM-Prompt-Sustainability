import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min([4, 5, 6, 7, 8, 9, 1, 2, 3], 0, 8), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min([1], 0, 0), 1)

    def test_edge_case_sorted_array(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8), 1)

    def test_boundary_case_duplicates(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7, 8, 8], 0, 8), 1)

    def test_corner_case_duplicates_at_end(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7, 8, 8, 8], 0, 10), 1)

    def test_corner_case_duplicates_at_start(self):
        self.assertEqual(find_Min([1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 10), 1)

    def test_corner_case_duplicates_in_middle(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7, 8, 8, 9], 0, 10), 1)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            find_Min([], 0, 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            find_Min([1, 2, 3, 4, 5, 6, 7, 8, 9], -1, 8)

    def test_invalid_input_out_of_range_index(self):
        with self.assertRaises(IndexError):
            find_Min([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 10)
