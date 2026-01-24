import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [Pair(1, 3), Pair(2, 4), Pair(3, 5), Pair(4, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_edge_case_single_element_array(self):
        arr = [Pair(1, 1)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_edge_case_all_elements_equal(self):
        arr = [Pair(1, 1), Pair(2, 2), Pair(3, 3)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_edge_case_all_elements_greater_than_previous(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_edge_case_all_elements_less_than_previous(self):
        arr = [Pair(4, 3), Pair(3, 2), Pair(2, 1)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)
