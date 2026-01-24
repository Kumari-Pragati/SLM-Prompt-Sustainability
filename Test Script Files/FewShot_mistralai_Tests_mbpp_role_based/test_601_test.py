import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):
    def test_positive_numbers(self):
        arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
        self.assertEqual(max_chain_length(arr, len(arr)), 3)

    def test_zero_and_one(self):
        arr = [Pair(0, 0), Pair(1, 1)]
        self.assertEqual(max_chain_length(arr, len(arr)), 2)

    def test_decreasing_numbers(self):
        arr = [Pair(5, 4), Pair(3, 2), Pair(1, 0)]
        self.assertEqual(max_chain_length(arr, len(arr)), 3)

    def test_increasing_numbers(self):
        arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
        self.assertEqual(max_chain_length(arr[::-1], len(arr)), 3)

    def test_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_negative_numbers(self):
        arr = [Pair(-1, -2), Pair(-3, -4), Pair(-5, -6)]
        self.assertEqual(max_chain_length(arr, len(arr)), 1)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            max_chain_length(arr, len(arr) - 1)

    def test_invalid_input_pair(self):
        with self.assertRaises(TypeError):
            max_chain_length([1, 2], 3)
