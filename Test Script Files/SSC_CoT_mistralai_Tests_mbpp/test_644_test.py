import unittest
from mbpp_644_code import range
from six.moves import xrange

from644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 2), [2, 1, 3, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 0), [5, 1, 2, 3, 4])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(reverse_Array_Upto_K([], 0), [])
        self.assertEqual(reverse_Array_Upto_K([], 1), [])
        self.assertEqual(reverse_Array_Upto_K([1], 0), [1])
        self.assertEqual(reverse_Array_Upto_K([1], 1), [])
        self.assertEqual(reverse_Array_Upto_K([1], 2), [])

        self.assertEqual(reverse_Array_Upto_K([1, 2], 0), [2])
        self.assertEqual(reverse_Array_Upto_K([1, 2], 1), [1])
        self.assertEqual(reverse_Array_Upto_K([1, 2], 2), [])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            reverse_Array_Upto_K([1, 2, 3], -1)
        with self.assertRaises(ValueError):
            reverse_Array_Upto_K([1, 2, 3], len([1, 2, 3]) + 1)
