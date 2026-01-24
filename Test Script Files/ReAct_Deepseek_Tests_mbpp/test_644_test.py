import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [2, 1, 3, 4, 5])

    def test_edge_case_k_equals_one(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 1), [5, 4, 3, 2, 1])

    def test_edge_case_k_equals_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])

    def test_edge_case_empty_array(self):
        self.assertEqual(reverse_Array_Upto_K([], 3), [])

    def test_edge_case_k_equals_zero(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
