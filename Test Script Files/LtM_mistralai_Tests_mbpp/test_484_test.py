import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [4, 5]), [1, 2, 3])
        self.assertListEqual(remove_matching_tuple([4, 5], [1, 2, 3]), [])
        self.assertListEqual(remove_matchingTuple([], [1, 2, 3]), [])
        self.assertListEqual(remove_matchingTuple([1, 2, 3], []), [1, 2, 3])

    def test_edge_cases(self):
        self.assertListEqual(remove_matchingTuple([0, 1, 2], [1, 2, 3]), [0])
        self.assertListEqual(remove_matchingTuple([1, 2, 3], [-1, 0, 1]), [2, 3])
        self.assertListEqual(remove_matchingTuple([-1, 0, 1], [1, 2, 3]), [-1, 0])
        self.assertListEqual(remove_matchingTuple([1, 2, 3], [1, 2, 3, 4]), [])

    def test_complex(self):
        self.assertListEqual(remove_matchingTuple([1, 2, 3], [(1, 2), (3, 4)]), [(3, 4)])
        self.assertListEqual(remove_matchingTuple([(1, 2), (3, 4)], [1, 2, 3]), [])
        self.assertListEqual(remove_matchingTuple([(1, 2), (3, 4)], [(1, 2), (3, 4), (5, 6)]), [(5, 6)])
