import unittest
from mbpp_601_code import max_chain_Length

class TestMaxChainLength(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4)], 4), 4)

    def test_edge_case_single_pair(self):
        self.assertEqual(max_chain_length([Pair(1, 2)], 1), 1)

    def test_edge_case_no_pairs(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_edge_case_increasing_order(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)], 5), 5)

    def test_edge_case_decreasing_order(self):
        self.assertEqual(max_chain_length([Pair(5, 4), Pair(4, 3), Pair(3, 2), Pair(2, 1)], 4), 4)

    def test_edge_case_duplicate_pairs(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 1)], 2), 2)

    def test_edge_case_out_of_order_pairs(self):
        self.assertEqual(max_chain_length([Pair(2, 1), Pair(1, 2)], 2), 2)
