import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 3, 2), [(3, 4, 5), (1, 2)])

    def test_edge_case_small_k(self):
        self.assertEqual(split_Arr([1, 2, 3], 3, 1), [(2, 3), [1]])

    def test_edge_case_large_k(self):
        self.assertEqual(split_Arr([1, 2, 3], 3, 4), [(1, 2, 3)])

    def test_edge_case_empty_array(self):
        self.assertEqual(split_Arr([], 3, 2), [ [], [] ])

    def test_edge_case_negative_k(self):
        with self.assertRaises(IndexError):
            split_Arr([1, 2, 3], 3, -1)

    def test_invalid_input_type_a(self):
        with self.assertRaises(TypeError):
            split_Arr('a', 3, 2)

    def test_invalid_input_type_n(self):
        with self.assertRaises(TypeError):
            split_Arr([1, 2, 3], 'a', 2)

    def test_invalid_input_type_k(self):
        with self.assertRaises(TypeError):
            split_Arr([1, 2, 3], 3, 'a' )
