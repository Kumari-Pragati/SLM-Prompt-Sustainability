import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_empty_array(self):
        self.assertRaises(IndexError, split_Arr, [], 1, 1)

    def test_single_element_array(self):
        self.assertEqual(split_Arr([1], 1, 1), [1])

    def test_simple_array(self):
        self.assertEqual(split_Arr([1, 2, 3, 4], 2, 2), [(2, 3, 4), (1)])

    def test_negative_k(self):
        self.assertRaises(ValueError, split_Arr, [1, 2, 3], 2, -1)

    def test_k_greater_than_n(self):
        self.assertRaises(ValueError, split_Arr, [1, 2, 3], 2, 4)

    def test_k_equal_n(self):
        self.assertEqual(split_Arr([1, 2, 3], 3, 3), [(1, 2), (3)])
