import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])

    def test_boundary_case_m_equals_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 2), [3, 4, 5, 1, 2])

    def test_boundary_case_m_greater_than_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 3, 2), [3, 4, 5, 1, 2])

    def test_boundary_case_m_equals_len_list(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 1), [2, 3, 4, 5, 1])

    def test_boundary_case_n_equals_0(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 0), [1, 2, 3, 4, 5])

    def test_boundary_case_m_equals_0(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 2), [2, 3, 4, 5, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(rotate_left([], 2, 1), [])

    def test_edge_case_negative_m(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], -2, 1), [2, 3, 4, 5, 1])

    def test_edge_case_negative_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, -1), [1, 2, 3, 4, 5])

    def test_edge_case_m_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 10, 2), [3, 4, 5, 1, 2])

    def test_edge_case_n_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 10), [1, 2, 3, 4, 5])
