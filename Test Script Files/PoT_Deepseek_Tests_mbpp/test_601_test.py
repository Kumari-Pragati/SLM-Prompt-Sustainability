import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_typical_case(self):
        pairs = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        self.assertEqual(max_chain_length(pairs, len(pairs)), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_boundary_case_single_element(self):
        pairs = [Pair(5, 24)]
        self.assertEqual(max_chain_length(pairs, 1), 1)

    def test_corner_case_no_valid_chain(self):
        pairs = [Pair(5, 24), Pair(39, 20), Pair(15, 10), Pair(27, 15), Pair(50, 40)]
        self.assertEqual(max_chain_length(pairs, len(pairs)), 0)

    def test_corner_case_same_values(self):
        pairs = [Pair(5, 5), Pair(39, 39), Pair(15, 15), Pair(27, 27), Pair(50, 50)]
        self.assertEqual(max_chain_length(pairs, len(pairs)), 1)
