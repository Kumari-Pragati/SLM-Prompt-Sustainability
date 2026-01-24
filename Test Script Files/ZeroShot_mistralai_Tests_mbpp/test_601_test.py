import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def setUp(self):
        self.arr = [
            Pair(1, 2),
            Pair(2, 3),
            Pair(3, 4),
            Pair(4, 5),
            Pair(5, 6),
            Pair(6, 7),
            Pair(7, 8),
            Pair(8, 9),
            Pair(9, 10),
        ]

    def test_empty_list(self):
        self.assertEqual(max_chain_length([], len([])), 0)

    def test_single_element_list(self):
        self.assertEqual(max_chain_length([Pair(1, 1)], 1), 1)

    def test_simple_chain(self):
        self.assertEqual(max_chain_length(self.arr, len(self.arr)), 7)

    def test_broken_chain(self):
        self.arr[2] = Pair(3, 2)
        self.assertEqual(max_chain_length(self.arr, len(self.arr)), 3)

    def test_reverse_chain(self):
        self.arr.reverse()
        self.assertEqual(max_chain_length(self.arr, len(self.arr)), 7)
