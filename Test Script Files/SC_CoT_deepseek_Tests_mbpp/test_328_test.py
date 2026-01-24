import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])

    def test_edge_case_m_equals_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 2), [3, 4, 5, 1, 2])

    def test_boundary_case_m_greater_than_list_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 3), [3, 4, 5, 1, 2])

    def test_boundary_case_n_greater_than_list_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 6), [3, 4, 5, 1, 2])

    def test_special_case_empty_list(self):
        self.assertEqual(rotate_left([], 2, 3), [])

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], -1, 3)

    def test_invalid_input_out_of_range_index(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 6, 3)
