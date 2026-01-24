import unittest
from mbpp_586_code import split_Arr

class TestSplit_Arr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 3, 2), [5, 6, [1, 2, 3]])

    def test_edge_case_k_zero(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 0, 2), [1, 2, 3, 4, 5, 6])

    def test_edge_case_k_equal_to_length(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 6, 2), [[1, 2, 3, 4, 5, 6]])

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 7, 2), [5, 6, [1, 2, 3, 4]])

    def test_edge_case_k_negative(self):
        with self.assertRaises(IndexError):
            split_Arr([1, 2, 3, 4, 5, 6], -1, 2)

    def test_edge_case_n_zero(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 0, 2), [5, 6, [1, 2, 3]])

    def test_edge_case_n_greater_than_length(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 10, 2), [5, 6, [1, 2, 3, 4, 5]])

    def test_edge_case_n_negative(self):
        with self.assertRaises(IndexError):
            split_Arr([1, 2, 3, 4, 5, 6], -1, 2)
