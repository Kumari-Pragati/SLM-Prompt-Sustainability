import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 2, 2), [3, 4, 5, 1, 2])
        self.assertEqual(split_Arr([6, 7, 8, 9], 2, 1), [8, 9, 6, 7])
        self.assertEqual(split_Arr([0, 1, 2, 3], 1, 0), [1, 2, 3, 0])

    def test_edge_cases(self):
        self.assertEqual(split_Arr([1], 1, 0), [1])
        self.assertEqual(split_Arr([1, 2], 1, 1), [2])
        self.assertEqual(split_Arr([1, 2], 2, 0), [2, 1])
        self.assertEqual(split_Arr([1, 2], 2, 2), [1, 2])

    def test_complex(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 2, 3), [4, 5, 1, 2, 3])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 3, 2), [3, 4, 5, 1, 2])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 4, 2), [2, 3, 4, 5, 1])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 2), [2, 3, 4, 5, 1])
