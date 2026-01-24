import unittest
from mbpp_869_code import List

from 869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_list_range([], 1, 2), [])

    def test_single_element(self):
        self.assertListEqual(remove_list_range([(1, 1)], 1, 2), [(1, 1)])
        self.assertListEqual(remove_list_range([(1, 1)], 0, 2), [])
        self.assertListEqual(remove_list_range([(1, 1)], 1, 3), [(1, 1)])

    def test_multiple_elements(self):
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3)], 1, 3), [(1, 1), (2, 2), (3, 3)])
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3)], 0, 2), [(2, 2)])
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3)], 1, 2), [(2, 2)])

    def test_negative_numbers(self):
        self.assertListEqual(remove_list_range([(-1, -1), (0, 0), (1, 1)], -2, 1), [(-1, -1), (0, 0)])
        self.assertListEqual(remove_list_range([(-1, -1), (0, 0), (1, 1)], -3, 1), [(-1, -1), (0, 0), (1, 1)])
        self.assertListEqual(remove_list_range([(-1, -1), (0, 0), (1, 1)], -1, 1), [(-1, -1), (0, 0)])
