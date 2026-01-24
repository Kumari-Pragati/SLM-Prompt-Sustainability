import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_reverse_Array_Upto_K(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 2), [4, 3, 2, 1, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 1), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 0), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([], 0), [])
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])
        self.assertEqual(reverse_Array_Upto_K([1, 2], 1), [2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2], 2), [2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 1), [3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 2), [3, 2, 1])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 3), [3, 2, 1])
