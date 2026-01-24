import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3, 4], [2, 3]), [1, 4])
        self.assertListEqual(remove_matchingTuple([5, 6, 7], []), [5, 6, 7])
        self.assertListEqual(remove_matchingTuple([], [1, 2]), [])

    def test_edge_cases(self):
        self.assertListEqual(remove_matchingTuple([], []), [])
        self.assertListEqual(remove_matchingTuple([1], [1]), [])
        self.assertListEqual(remove_matchingTuple([1, 1], [1]), [])
        self.assertListEqual(remove_matchingTuple([1, 2, 1], [1, 2]), [2])

    def test_boundary_cases(self):
        self.assertListEqual(remove_matchingTuple([0, 1, 2, 3], [1, 2, 3, 4]), [0])
        self.assertListEqual(remove_matchingTuple([-1, 0, 1, 2], [-1, 0, 1, 2]), [])
        self.assertListEqual(remove_matchingTuple([1, 2, 3, 4], [-1, 0, 1, 2]), [3, 4])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_matchingTuple, "string", [1, 2])
        self.assertRaises(TypeError, remove_matchingTuple, [1, 2], "string")
