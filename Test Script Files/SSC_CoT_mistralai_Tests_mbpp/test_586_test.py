import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 3, 2), [(3, 4, 5), (1, 2)])
        self.assertEqual(split_Arr([6, 7, 8, 9], 2, 2), [(8, 9), (6, 7)])

    def test_edge_cases(self):
        self.assertEqual(split_Arr([1], 1, 1), [[]])
        self.assertEqual(split_Arr([1], 1, 2), [[]])
        self.assertEqual(split_Arr([1, 2], 1, 1), [[2]])
        self.assertEqual(split_Arr([1, 2], 1, 2), [[]])
        self.assertEqual(split_Arr([1, 2], 2, 0), [[1, 2]])
        self.assertEqual(split_Arr([1, 2], 2, 3), [[1, 2]])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            split_Arr([1], -1, 1)
        with self.assertRaises(ValueError):
            split_Arr([1], 1, -1)
        with self.assertRaises(ValueError):
            split_Arr([1], 0, 1)
        with self.assertRaises(ValueError):
            split_Arr([1], 1, 0)
        with self.assertRaises(ValueError):
            split_Arr([], 1, 1)
