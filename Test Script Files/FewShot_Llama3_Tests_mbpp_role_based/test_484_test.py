import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(remove_matching_tuple([], []), [])

    def test_no_matching_tuples(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3], [4, 5, 6]), [1, 2, 3])

    def test_some_matching_tuples(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3, 4], [2, 4]), [1, 3])

    def test_all_matching_tuples(self):
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3, 3, 3], [1, 2, 3]), [])

    def test_lists_with_duplicates(self):
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 3]), [])

    def test_lists_with_duplicates_and_non_matching(self):
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3, 3, 3, 4], [1, 2, 2, 3, 3]), [4])
