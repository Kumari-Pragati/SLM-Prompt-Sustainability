import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 2), [3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])

    def test_edge_cases(self):
        self.assertEqual(reverse_Array_Upto_K([], 1), [])
        self.assertEqual(reverse_Array_Upto_K([1], 0), [1])
        self.assertEqual(reverse_Array_Upto_K([1, 2], 0), [2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2], 2), [1, 2])

    def test_complex(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 3), [3, 2, 1, 4, 5, 6])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 5), [5, 4, 3, 2, 1, 6])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 6), [6, 5, 4, 3, 2, 1])
