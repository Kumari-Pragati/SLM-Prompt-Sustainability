import unittest
from mbpp_601_code import Iterable
from six.moves import range

class TestMaxChainLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element(self):
        for pair in [Pair(1, 1), Pair(1, 2), Pair(2, 1)]:
            self.assertEqual(max_chain_length([pair], 1), 1)

    def test_simple_chain(self):
        pairs = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        self.assertEqual(max_chain_length(pairs, len(pairs)), 4)

    def test_complex_chain(self):
        pairs = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9), Pair(9, 10), Pair(10, 11), Pair(11, 12), Pair(12, 13), Pair(13, 14), Pair(14, 15), Pair(15, 16), Pair(16, 17), Pair(17, 18), Pair(18, 19), Pair(19, 20), Pair(20, 21), Pair(21, 22), Pair(22, 23), Pair(23, 24), Pair(24, 25), Pair(25, 26), Pair(26, 27), Pair(27, 28), Pair(28, 29), Pair(29, 30)]
        self.assertEqual(max_chain_length(pairs, len(pairs)), 30)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_chain_length([1, 2], 3)
        with self.assertRaises(TypeError):
            max_chain_length([Pair(1, 2), Pair(3, 4)], 'invalid')
        with self.assertRaises(ValueError):
            max_chain_length([], -1)
        with self.assertRaises(ValueError):
            max_chain_length([Pair(1, 2)], -1)
        with self.assertRaises(ValueError):
            max_chain_length([Pair(1, 2)], 0)
