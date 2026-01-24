import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [2, 1, 3, 4, 5])

    def test_boundary_case(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge_case(self):
        self.assertEqual(reverse_Array_Upto_K([], 3), [])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_Array_Upto_K("1, 2, 3, 4, 5", 3)
        with self.assertRaises(TypeError):
            reverse_Array_Upto_K([1, 2, 3, 4, 5], "3")
