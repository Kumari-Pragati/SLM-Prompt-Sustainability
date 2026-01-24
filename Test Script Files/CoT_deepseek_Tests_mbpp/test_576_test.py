import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3, 4]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case(self):
        A = [1, 2, 3, 4, 5]
        B = []
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_invalid_input(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3, 'a']
        with self.assertRaises(TypeError):
            is_Sub_Array(A, B, len(A), len(B))

    def test_invalid_input_empty_list(self):
        A = []
        B = [2, 3, 4]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_invalid_input_negative_numbers(self):
        A = [1, -2, 3, 4, 5]
        B = [-2, 3, 4]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))
