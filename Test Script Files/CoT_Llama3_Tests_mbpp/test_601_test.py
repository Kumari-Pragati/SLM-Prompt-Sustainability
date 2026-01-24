import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_typical_case(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)]
        self.assertEqual(max_chain_length(arr, len(arr)), 4)

    def test_edge_case(self):
        arr = [Pair(1, 2), Pair(2, 1)]
        self.assertEqual(max_chain_length(arr, len(arr)), 2)

    def test_single_element(self):
        arr = [Pair(1, 1)]
        self.assertEqual(max_chain_length(arr, len(arr)), 1)

    def test_empty_array(self):
        arr = []
        self.assertEqual(max_chain_length(arr, len(arr)), 0)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        with self.assertRaises(TypeError):
            max_chain_length(arr, len(arr))
