import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 2), [2, 1, 3, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(reverse_Array_Upto_K([], 1), [])

    def test_edge_case_single_element(self):
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])

    def test_edge_case_k_greater_than_len(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 4), [1, 2, 3])

    def test_edge_case_k_less_than_zero(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], -1), [3, 2, 1])

    def test_corner_case_k_equal_zero(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 0), [])
