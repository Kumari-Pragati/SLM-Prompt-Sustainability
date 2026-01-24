import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])
        self.assertListEqual(remove_list_range([10, 20, 30, 40], 20, 30), [20, 30])
        self.assertListEqual(remove_list_range([-1, 0, 1], -1, 1), [-1])

    def test_edge_and_boundary(self):
        self.assertListEqual(remove_list_range([], 1, 2), [])
        self.assertListEqual(remove_list_range([1], 1, 1), [])
        self.assertListEqual(remove_list_range([1, 2], 0, 0), [])
        self.assertListEqual(remove_list_range([1, 2], 3, 3), [])
        self.assertListEqual(remove_list_range([1, 2], 1, 2), [1, 2])
        self.assertListEqual(remove_list_range([1, 2], -1, 0), [])
        self.assertListEqual(remove_list_range([1, 2], 3, 4), [])

    def test_complex(self):
        self.assertListEqual(remove_list_range([[1, 2], [3, 4]], 1.5, 2.5), [[3, 4]])
        self.assertListEqual(remove_list_range([[1, 2], [3, 4]], -1, 0), [])
        self.assertListEqual(remove_list_range([[1, 2], [3, 4]], 3, 4), [[1, 2]])
        self.assertListEqual(remove_list_range([[1, 2], [3, 4]], 1, 3), [[1, 2]])
        self.assertListEqual(remove_list_range([[1, 2], [3, 4]], -1, 5), [[1, 2], [3, 4]])
