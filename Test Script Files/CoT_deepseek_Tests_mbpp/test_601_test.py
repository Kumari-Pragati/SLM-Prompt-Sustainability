import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):
    def test_typical_case(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_single_element(self):
        arr = [Pair(5, 24)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_reverse_sorted_array(self):
        arr = [Pair(50, 24), Pair(39, 23), Pair(15, 10), Pair(27, 1), Pair(5, 0)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_duplicate_pairs(self):
        arr = [Pair(5, 24), Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_chain_length("invalid_input", 5)
