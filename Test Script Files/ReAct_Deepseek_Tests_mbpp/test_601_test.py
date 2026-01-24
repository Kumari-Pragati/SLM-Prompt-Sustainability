import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_typical_case(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case_single_element(self):
        arr = [Pair(5, 24)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_edge_case_empty_list(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_explicitly_handled_error_case_invalid_input(self):
        arr = [Pair(5, 24), Pair(39, 60), 'invalid_input', Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        with self.assertRaises(TypeError):
            max_chain_length(arr, n)
