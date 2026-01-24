import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_typical_input(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_edge_case(self):
        arr = [Pair(1, 2), Pair(2, 1), Pair(3, 4), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

    def test_edge_case2(self):
        arr = [Pair(1, 2), Pair(2, 2), Pair(3, 4), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case3(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 3), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case4(self):
        arr = [Pair(1, 2), Pair(2, 2), Pair(3, 4), Pair(4, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        with self.assertRaises(TypeError):
            max_chain_length(arr, n)

    def test_empty_input(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_single_element_input(self):
        arr = [Pair(1, 1)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)
