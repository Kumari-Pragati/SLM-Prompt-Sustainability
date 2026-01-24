import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [4, 3, 1] + [5, 2, 1])

    def test_edge_case_k_at_start(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 1), [4, 3, 2, 1] + [5])

    def test_edge_case_k_at_end(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 5), [4, 3, 2, 1] + [])

    def test_edge_case_k_at_middle(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 2), [4, 3, 2] + [1, 5])

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 10), [4, 3, 2, 1] + [5])

    def test_edge_case_k_zero(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 0), [5, 4, 3, 2, 1])

    def test_edge_case_k_negative(self):
        with self.assertRaises(IndexError):
            reverse_Array_Upto_K([1, 2, 3, 4, 5], -1)
