import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_edge_case_m_equals_n(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 2), [3, 4, 5, 1, 2])

    def test_boundary_case_m_equals_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 1), [5, 1, 2, 3, 4])

    def test_boundary_case_n_equals_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 5), [4, 5, 1, 2, 3])

    def test_invalid_input_m_greater_than_length(self):
        with self.assertRaises(IndexError):
            rotate_right([1, 2, 3, 4, 5], 6, 1)

    def test_invalid_input_n_greater_than_length(self):
        with self.assertRaises(IndexError):
            rotate_right([1, 2, 3, 4, 5], 2, 6)
