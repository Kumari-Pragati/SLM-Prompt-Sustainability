import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 2), 4)

    def test_edge_case_k_equal_to_m(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 3), 5)

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 3), 5)

    def test_edge_case_k_greater_than_m(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 4), 6)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 4), 6)

    def test_edge_case_k_equal_to_m_plus_n(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 6), 6)

    def test_edge_case_k_greater_than_m_plus_n(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 7), None)

    def test_invalid_input_m_zero(self):
        with self.assertRaises(IndexError):
            find_kth([1, 3, 5], [2, 4, 6], 0, 3, 2)

    def test_invalid_input_n_zero(self):
        with self.assertRaises(IndexError):
            find_kth([1, 3, 5], [2, 4, 6], 3, 0, 2)

    def test_invalid_input_k_zero(self):
        with self.assertRaises(IndexError):
            find_kth([1, 3, 5], [2, 4, 6], 3, 3, 0)

    def test_invalid_input_k_greater_than_m_plus_n(self):
        with self.assertRaises(IndexError):
            find_kth([1, 3, 5], [2, 4, 6], 3, 3, 7)
