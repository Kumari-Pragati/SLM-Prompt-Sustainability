import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2), [4, 5, 6, 7, 8, 9, 1, 2])

    def test_boundary_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 1), [2, 3, 4, 5, 6, 7, 8, 9, 1])

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            split_Arr([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 1)
