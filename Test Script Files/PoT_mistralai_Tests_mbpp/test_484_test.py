import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(remove_matching_tuple([], []), [])
        self.assertListEqual(remove_matching_tuple([], [(1, 2)]), [])
        self.assertListEqual(remove_matching_tuple([(1, 2)], []), [(1, 2)])

    def test_single_elements(self):
        self.assertListEqual(remove_matching_tuple([1], [2]), [1])
        self.assertListEqual(remove_matching_tuple([(1, 2)], [(1, 3)]), [(1, 2)])

    def test_simple_lists(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [2, 4]), [1, 3])
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(2, 3), (1, 5)]), [(3, 4)])

    def test_lists_with_duplicates(self):
        self.assertListEqual(remove_matching_tuple([1, 1, 2, 3], [2, 1]), [3])
        self.assertListEqual(remove_matching_tuple([(1, 2), (1, 2), (3, 4)], [(2, 1), (1, 2)]), [(3, 4)])

    def test_lists_with_matching_elements(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [2, 1, 3]), [])
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(2, 1), (1, 2)]), [])

    def test_lists_with_nested_tuples(self):
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(2, 1), (1, (3, 4))]), [(3, 4)])
        self.assertListEqual(remove_matching_tuple([(1, 2), (3, 4)], [(2, 1), (1, (3, 4)), (1, 2)]), [])
