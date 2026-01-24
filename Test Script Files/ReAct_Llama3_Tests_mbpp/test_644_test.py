import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(reverse_Array_Upto_K([], 0), [])

    def test_single_element_array(self):
        self.assertEqual(reverse_Array_Upto_K([1], 0), [1])

    def test_k_greater_than_array_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 5), [3, 2, 1])

    def test_k_equal_to_array_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 3), [3, 2, 1])

    def test_k_less_than_array_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 2), [4, 3, 2, 1, 5])

    def test_k_zero(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 0), [3, 2, 1])

    def test_k_negative(self):
        with self.assertRaises(IndexError):
            reverse_Array_Upto_K([1, 2, 3], -1)
