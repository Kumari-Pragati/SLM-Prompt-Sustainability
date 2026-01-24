import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(reverse_Array_Upto_K([], 0), [])

    def test_single_element(self):
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])

    def test_k_greater_than_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 4), [1, 2, 3])

    def test_k_less_than_zero(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], -1), [3, 2, 1])

    def test_k_equal_to_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 3), [3, 2, 1])

    def test_k_at_start(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 1), [2, 3])

    def test_k_at_end(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 3), [3])

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, reverse_Array_Upto_K, [1, 2, 'a'], 2)

    def test_negative_numbers(self):
        self.assertEqual(reverse_Array_Upto_K([-1, 2, -3], 1), [2, -3])
