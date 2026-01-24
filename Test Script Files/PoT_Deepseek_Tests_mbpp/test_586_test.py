import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 2), [4, 5, 1, 2, 3])

    def test_edge_case_k_equals_zero(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])

    def test_edge_case_k_equals_n(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 5), [1, 2, 3, 4, 5])

    def test_boundary_case_k_greater_than_n(self):
        with self.assertRaises(IndexError):
            split_Arr([1, 2, 3, 4, 5], 5, 6)

    def test_boundary_case_n_equals_zero(self):
        self.assertEqual(split_Arr([], 0, 2), [])

    def test_corner_case_empty_array(self):
        self.assertEqual(split_Arr([], 0, 0), [])
