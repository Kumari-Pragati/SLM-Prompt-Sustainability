import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(remove_matching_tuple([], []), [])

    def test_single_elements(self):
        self.assertListEqual(remove_matching_tuple([1], [1]), [])
        self.assertListEqual(remove_matching_tuple([], [1]), [])

    def test_identical_lists(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [1, 2, 3]), [])

    def test_no_matches(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [4, 5, 6]), [1, 2, 3])

    def test_multiple_matches(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 1, 3], [1, 2, 1]), [3])

    def test_lists_with_tuples(self):
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(1, 2), (3, 4), (1, 5)]), [])
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(3, 4), (1, 2)]), [])
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(5, 6), (1, 2)]), [(3, 4)])

    def test_lists_with_different_types(self):
        self.assertRaises(TypeError, remove_matching_tuple, [1, 2, 3], [1, 2, "3"])
