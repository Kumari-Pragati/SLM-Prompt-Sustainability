import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):
    def test_simple(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        self.assertEqual(max_chain_length(arr, len(arr)), 3)

    def test_edge_case_empty(self):
        arr = []
        self.assertEqual(max_chain_length(arr, len(arr)), 0)

    def test_edge_case_single(self):
        arr = [Pair(1, 2)]
        self.assertEqual(max_chain_length(arr, len(arr)), 1)

    def test_edge_case_max_chain(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)]
        self.assertEqual(max_chain_length(arr, len(arr)), 4)

    def test_edge_case_min_chain(self):
        arr = [Pair(5, 4), Pair(4, 3), Pair(3, 2), Pair(2, 1)]
        self.assertEqual(max_chain_length(arr, len(arr)), 1)

    def test_edge_case_chain_of_length_2(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 1)]
        self.assertEqual(max_chain_length(arr, len(arr)), 2)

    def test_edge_case_chain_of_length_3(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6)]
        self.assertEqual(max_chain_length(arr, len(arr)), 5)
