import unittest
from mbpp_943_code import merge
from 943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(combine_lists([], []), [])

    def test_one_element_lists(self):
        self.assertListEqual(combine_lists([1], []), [1])
        self.assertListEqual(combine_lists([], [1]), [1])

    def test_same_length_lists(self):
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_different_length_lists(self):
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5])
        self.assertListEqual(combine_lists([1, 2, 3], [4]), [1, 2, 3, 4])
        self.assertListEqual(combine_lists([1], [2, 3, 4]), [1, 2, 3, 4])
