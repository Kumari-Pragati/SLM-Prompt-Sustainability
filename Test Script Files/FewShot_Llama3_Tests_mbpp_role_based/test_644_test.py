import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverse_Array_Upto_K(unittest.TestCase):
    def test_typical_use_case(self):
        input = [1, 2, 3, 4, 5, 6]
        k = 3
        expected_output = [4, 5, 6, 1, 2, 3]
        self.assertEqual(reverse_Array_Upto_K(input, k), expected_output)

    def test_edge_case_k_at_start(self):
        input = [1, 2, 3, 4, 5, 6]
        k = 1
        expected_output = [6, 1, 2, 3, 4, 5]
        self.assertEqual(reverse_Array_Upto_K(input, k), expected_output)

    def test_edge_case_k_at_end(self):
        input = [1, 2, 3, 4, 5, 6]
        k = 6
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(reverse_Array_Upto_K(input, k), expected_output)

    def test_edge_case_k_equal_to_length(self):
        input = [1, 2, 3, 4, 5, 6]
        k = 6
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(reverse_Array_Upto_K(input, k), expected_output)

    def test_edge_case_k_greater_than_length(self):
        input = [1, 2, 3, 4, 5, 6]
        k = 7
        with self.assertRaises(IndexError):
            reverse_Array_Upto_K(input, k)
