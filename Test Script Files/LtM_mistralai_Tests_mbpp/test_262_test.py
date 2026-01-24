import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))
        self.assertEqual(split_two_parts([0, 0, 0, 0, 0], 3), ([0, 0, 0], [0]))
        self.assertEqual(split_two_parts(['a', 'b', 'c', 'd', 'e'], 3), (['a', 'b', 'c'], ['d', 'e']))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 6), ([1, 2, 3, 4, 5], []))
        self.assertEqual(split_two_parts([], 2), ([], []))
        self.assertEqual(split_two_parts(['a', 'b', 'c', 'd', 'e'], 0), ([], ['a', 'b', 'c', 'd', 'e']))
        self.assertEqual(split_two_parts(['a', 'b', 'c', 'd', 'e'], 6), (['a', 'b', 'c', 'd', 'e'], []))
        self.assertEqual(split_two_parts([], 2), ([], []))
