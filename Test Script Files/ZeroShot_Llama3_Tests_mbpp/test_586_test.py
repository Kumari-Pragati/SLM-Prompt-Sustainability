import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_split_Arr(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 2, 3), [1, 2, 4, 5, 6, 1, 2, 3, 4])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 3, 2), [1, 2, 3, 4, 5, 6, 1, 2, 3])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 4, 3), [1, 2, 3, 4, 5, 6, 1, 2, 3, 4])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 5, 4), [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5, 6], 6, 5), [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])

    def test_split_Arr_edge_cases(self):
        self.assertEqual(split_Arr([1], 1, 1), [1, 1])
        self.assertEqual(split_Arr([1], 1, 0), [1])
        self.assertEqual(split_Arr([1], 0, 0), [1])
        self.assertEqual(split_Arr([], 1, 1), [])
