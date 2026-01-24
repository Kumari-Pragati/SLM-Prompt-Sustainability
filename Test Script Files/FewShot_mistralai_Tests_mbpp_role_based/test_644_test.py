import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(reverse_Array_Upto_K([], 0), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_Array_Upto_K([1], 0), [1])
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])

    def test_positive_k_less_than_len(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4], 2), [3, 4])

    def test_positive_k_equal_to_len(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4], 4), [1, 2, 3])

    def test_negative_k(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4], -1), [4, 3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4], -2), [3, 4, 1, 2])

    def test_k_greater_than_len(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4], 5), [1, 2, 3, 4])
