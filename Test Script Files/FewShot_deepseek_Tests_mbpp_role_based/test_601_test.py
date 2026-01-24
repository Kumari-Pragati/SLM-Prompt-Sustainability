import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):
    def test_typical_case(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case(self):
        arr = [Pair(5, 24)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_boundary_case(self):
        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_invalid_input(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        with self.assertRaises(TypeError):
            max_chain_length(arr, 'invalid_input')

        with self.assertRaises(TypeError):
            max_chain_length('invalid_input', n)

        with self.assertRaises(TypeError):
            max_chain_length('invalid_input1', 'invalid_input2')
