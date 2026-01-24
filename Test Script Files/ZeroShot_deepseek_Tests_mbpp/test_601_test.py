import unittest
from mbpp_601_code import max_chain_length, Pair

class TestMaxChainLength(unittest.TestCase):
    def test_max_chain_length(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

        arr = [Pair(11, 20), Pair(17, 30), Pair(23, 35), Pair(37, 40), Pair(43, 50)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

        arr = [Pair(10, 20), Pair(15, 25), Pair(20, 30)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)
