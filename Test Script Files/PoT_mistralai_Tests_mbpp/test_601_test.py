import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4)], 4), 4)
        self.assertEqual(max_chain_length([Pair(1, 1), Pair(2, 2), Pair(3, 3)], 3), 3)
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 1), Pair(3, 4)], 4), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(max_chain_length([Pair(1, 1)], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_edge_case_invalid_input(self):
        self.assertRaises(TypeError, max_chain_length, [1, 2], 3)
        self.assertRaises(TypeError, max_chain_length, [Pair(1, 2)], 0.5)
