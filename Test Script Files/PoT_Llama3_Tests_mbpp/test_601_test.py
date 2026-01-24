import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_typical_case(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_edge_case(self):
        arr = [Pair(1, 1), Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case2(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_edge_case3(self):
        arr = [Pair(1, 2), Pair(2, 2), Pair(3, 4), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case4(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 3), Pair(4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case5(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(5, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case6(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_invalid_input(self):
        arr = [Pair(1, 2)]
        n ='string'
        with self.assertRaises(TypeError):
            max_chain_length(arr, n)
