import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(remove_matching_tuple([], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(remove_matching_tuple([1], []), [1])
        self.assertListEqual(remove_matching_tuple([], [1]), [])

    def test_identical_lists(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [1, 2, 3]), [])

    def test_non_matching_elements(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [4, 5, 6]), [1, 2, 3])

    def test_matching_elements(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [2, 3, 4]), [1])

    def test_mixed_lists(self):
        self.assertListEqual(remove_matching_tuple([1, 2, 3], [3, 4, 5]), [1, 2])
        self.assertListEqual(remove_matching_tuple([3, 4, 5], [1, 2, 3]), [4, 5])
