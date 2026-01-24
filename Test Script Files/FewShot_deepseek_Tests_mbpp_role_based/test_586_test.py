import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 2), [3, 4, 5, 1, 2])

    def test_boundary_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 5), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(split_Arr([1], 1, 0), [1])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 6), [2, 3, 4, 5, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_Arr([1, 2, 3, 4, 5], 'a', 2)
        with self.assertRaises(TypeError):
            split_Arr([1, 2, 3, 4, 5], 5, 'b')
        with self.assertRaises(TypeError):
            split_Arr([1, 2, 3, 4, 5], 'a', 'b')
        with self.assertRaises(IndexError):
            split_Arr([1, 2, 3, 4, 5], 5, 6)
