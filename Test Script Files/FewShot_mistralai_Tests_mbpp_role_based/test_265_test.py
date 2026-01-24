import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(list_split([], 3), [[]])

    def test_single_element_list(self):
        self.assertEqual(list_split([1], 3), [[]])

    def test_positive_numbers(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 2), [[1, 3], [2, 4]])

    def test_negative_step(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], -2), [[5, 3], [1]])

    def test_zero_step(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 0), [[]])
