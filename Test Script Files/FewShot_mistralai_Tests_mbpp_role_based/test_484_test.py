import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(remove_matching_tuple([], []), [])
        self.assertListEqual(remove_matching_tuple([], [(1, 2)]), [])
        self.assertListEqual(remove_matching_tuple([(1, 2)], []), [(1, 2)])

    def test_single_match(self):
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(1, 2)]), [(3, 4)])

    def test_multiple_matches(self):
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4), (1, 2)], [(1, 2)]), [(3, 4)])

    def test_no_matches(self):
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(5, 6)]), [(1, 2), (3, 4)])

    def test_lists_with_duplicates(self):
        self.assertListEqual(remove_matching_tuple([(1, 2), (1, 2)], [(1, 2)]), [])

    def test_lists_with_non_tuples(self):
        self.assertRaises(TypeError, remove_matching_tuple, [1, 2], [(1, 2)])
