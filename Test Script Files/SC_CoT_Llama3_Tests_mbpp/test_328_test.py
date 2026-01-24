import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 4), [3, 4, 5, 1, 2])

    def test_edge_case_m_equal_to_0(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 4), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 4, 4), [1, 2, 3, 4, 5])

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 4), [1, 2, 3, 4, 5])

    def test_edge_case_n_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 10), [3, 4, 5, 1, 2])

    def test_edge_case_m_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 10, 4), [1, 2, 3, 4, 5])

    def test_edge_case_n_equal_to_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 5), [3, 4, 5, 1, 2])

    def test_edge_case_m_equal_to_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 5), [1, 2, 3, 4, 5])

    def test_edge_case_m_greater_than_length_n_equal_to_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 5), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 6), [1, 2, 3, 4, 5])

    def test_edge_case_m_greater_than_length_n_equal_to_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 5), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_equal_to_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 6), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 7), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_greater_than_length_n_equal_to_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 7), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_greater_than_length_n_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 8), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_greater_than_length_n_greater_than_length_m_equal_to_n(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 8), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_greater_than_length_n_greater_than_length_m_greater_than_length(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 6, 9), [1, 2, 3, 4, 5])

    def test_edge_case_m_equal_to_length_n_greater_than_length_m_greater_than_length_n_greater_than_length_m_greater