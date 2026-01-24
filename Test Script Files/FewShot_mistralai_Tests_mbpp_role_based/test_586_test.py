import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 3, 2), [(3, 4, 5), (1, 2)])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 2, 3), [(4, 5), (1, 2), (3)])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 1, 5), [(4, 5), (1, 2, 3)])

    def test_empty_list(self):
        self.assertEqual(split_Arr([], 3, 2), [[], []])

    def test_negative_n(self):
        self.assertRaises(ValueError, split_Arr, [1, 2, 3], -1, 2)

    def test_negative_k(self):
        self.assertRaises(ValueError, split_Arr, [1, 2, 3], 3, -1)
