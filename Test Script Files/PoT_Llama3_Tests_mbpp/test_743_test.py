import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_edge_case_m_zero(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 1), [1, 2, 3, 4, 5])

    def test_edge_case_n_zero(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 0), [3, 4, 5, 1, 2])

    def test_edge_case_m_equal_n(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 2), [4, 5, 1, 2, 3])

    def test_edge_case_m_greater_than_list_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 10, 1), [3, 4, 5, 1, 2, 3])

    def test_edge_case_n_greater_than_list_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 1, 10), [1, 2, 3, 4, 5])

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 3), [3, 4, 5, 1, 2])

    def test_edge_case_n_greater_than_m(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 3, 5), [1, 2, 3, 4, 5])
