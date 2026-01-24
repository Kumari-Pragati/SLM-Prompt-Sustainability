import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_simple_combination(self):
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_empty_lists(self):
        self.assertListEqual(combine_lists([], []), [])

    def test_single_list(self):
        self.assertListEqual(combine_lists([1, 2, 3], []), [1, 2, 3])
        self.assertListEqual(combine_lists([], [1, 2, 3]), [1, 2, 3])

    def test_reverse_order(self):
        self.assertListEqual(combine_lists([3, 2, 1], [6, 5, 4]), [6, 5, 4, 3, 2, 1])

    def test_duplicates(self):
        self.assertListEqual(combine_lists([1, 2, 2, 3], [4, 5, 5]), [1, 2, 2, 3, 4, 5])

    def test_large_numbers(self):
        self.assertListEqual(combine_lists([1000000001, 1000000002], [1000000003, 1000000004]),
                              [1000000001, 1000000002, 1000000003, 1000000004])
