import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(list_split([], 3), [[]])

    def test_single_element_list(self):
        self.assertListEqual(list_split([1], 3), [[1]])

    def test_simple_list(self):
        self.assertListEqual(list_split([1, 2, 3, 4, 5], 2), [[1, 3], [2, 4], [5]])

    def test_negative_step(self):
        self.assertRaises(ValueError, lambda: list_split([1, 2, 3], -1))

    def test_zero_step(self):
        self.assertRaises(ValueError, lambda: list_split([1, 2, 3], 0))

    def test_step_larger_than_list_length(self):
        self.assertListEqual(list_split([1, 2, 3], 4), [[]])
