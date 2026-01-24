import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 3), [4, 5, 6, 7, 8, 9, 1, 2, 3])

    def test_edge_case_k_equals_zero(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_k_equals_n(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(split_Arr([], 0, 3), [])

    def test_invalid_input_k_greater_than_n(self):
        with self.assertRaises(AssertionError):
            split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 10)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(AssertionError):
            split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, -3)
