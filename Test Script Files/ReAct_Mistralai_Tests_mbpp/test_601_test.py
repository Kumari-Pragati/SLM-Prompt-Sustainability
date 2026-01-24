import unittest
from mbpp_601_code import range
from six.moves import xrange

class TestMaxChainLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element(self):
        for pair in [Pair(1, 1), Pair(1, 2), Pair(2, 1), Pair(2, 2)]:
            self.assertEqual(max_chain_length([pair], 1), 1)

    def test_two_elements(self):
        for pair1, pair2 in [
                (Pair(1, 2), Pair(2, 3)),
                (Pair(1, 2), Pair(3, 2)),
                (Pair(2, 1), Pair(1, 3)),
                (Pair(2, 1), Pair(3, 1)),
                (Pair(2, 2), Pair(1, 3)),
                (Pair(2, 2), Pair(3, 2))
        ]:
            self.assertEqual(max_chain_length([pair1, pair2], 2), 2)

    def test_three_elements(self):
        for pair1, pair2, pair3 in [
                (Pair(1, 2), Pair(2, 3), Pair(3, 4)),
                (Pair(1, 2), Pair(3, 2), Pair(2, 4)),
                (Pair(1, 2), Pair(4, 2), Pair(2, 3)),
                (Pair(2, 1), Pair(1, 3), Pair(3, 4)),
                (Pair(2, 1), Pair(3, 4), Pair(1, 3)),
                (Pair(2, 1), Pair(4, 1), Pair(1, 3)),
                (Pair(2, 2), Pair(1, 3), Pair(3, 4)),
                (Pair(2, 2), Pair(3, 3), Pair(1, 4)),
                (Pair(2, 2), Pair(3, 4), Pair(1, 3))
        ]:
            self.assertEqual(max_chain_length([pair1, pair2, pair3], 3), 3)

    def test_longer_list(self):
        arr = [Pair(i, i+1) for i in range(10)] + [Pair(10, 1)]
        self.assertEqual(max_chain_length(arr, len(arr)), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_chain_length([1, 2], 'not a number')
        with self.assertRaises(IndexError):
            max_chain_length([Pair(1, 2)], -1)
        with self.assertRaises(ValueError):
            max_chain_length([Pair(1, 2)], 0)
