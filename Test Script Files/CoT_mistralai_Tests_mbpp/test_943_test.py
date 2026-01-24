import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(combine_lists([]), [])
        self.assertListEqual(combine_lists([], [1]), [1])
        self.assertListEqual(combine_lists([], [1, 2]), [1, 2])

    def test_single_list(self):
        self.assertListEqual(combine_lists([1]), [1])
        self.assertListEqual(combine_lists([1, 2]), [1, 2])
        self.assertListEqual(combine_lists([2, 1]), [1, 2])

    def test_two_lists_same_elements(self):
        self.assertListEqual(combine_lists([1, 2], [2, 1]), [1, 2])

    def test_two_lists_different_elements(self):
        self.assertListEqual(combine_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertListEqual(combine_lists([3, 4], [1, 2]), [1, 2, 3, 4])

    def test_two_lists_mixed_types(self):
        self.assertListEqual(combine_lists([1, 2], [3, "a"]), [1, 2, 3, "a"])
        self.assertListEqual(combine_lists([3, "a"], [1, 2]), [1, 2, 3, "a"])

    def test_two_lists_one_empty(self):
        self.assertListEqual(combine_lists([], [1, 2]), [1, 2])
        self.assertListEqual(combine_lists([1, 2], []), [1, 2])

    def test_two_lists_one_negative(self):
        self.assertListEqual(combine_lists([-1, 0], [1, 2]), [-1, 0, 1, 2])
        self.assertListEqual(combine_lists([1, 2], [-1, 0]), [1, 2, -1, 0])
