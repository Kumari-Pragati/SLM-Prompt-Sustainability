import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(reverse_Array_Upto_K([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])

    def test_k_greater_than_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 4), [1, 2, 3])

    def test_k_equal_to_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 3), [3, 2, 1])

    def test_k_less_than_length(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 1), [3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 2), [2, 1])
