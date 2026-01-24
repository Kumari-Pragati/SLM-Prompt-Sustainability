import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 3), ([1, 2, 3], [4, 5]))

    def test_edge_cases(self):
        self.assertEqual(split_two_parts([1, 2, 3], 0), ([], [1, 2, 3]))
        self.assertEqual(split_two_parts([1, 2, 3], 5), ([1, 2, 3], []))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            split_two_parts("abc", 3)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            split_two_parts([1, 2, 3], -1)

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            split_two_parts([1, 2, 3], 6)
