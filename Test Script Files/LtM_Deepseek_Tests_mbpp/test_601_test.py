import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_simple_case(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_edge_case_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_boundary_case_single_element(self):
        arr = [Pair(5, 24)]
        n = 1
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_complex_case_no_chain(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90), Pair(10, 15)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

    def test_complex_case_with_chain(self):
        arr = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90), Pair(11, 22), Pair(17, 33)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)
