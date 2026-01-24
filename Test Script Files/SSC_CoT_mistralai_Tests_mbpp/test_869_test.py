import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 3, 5), [(3, 4)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 2, 6), [(1, 2), (3, 4), (5, 6)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 1, 7), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_edge_input(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 0, 5), [])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 4, 6), [])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], -1, 5), [])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 4, 7), [(7, 8)])

    def test_boundary_input(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 1, 5), [(1, 2), (3, 4)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 3, 5), [(3, 4)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 2, 6), [(1, 2), (3, 4), (5, 6)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_list_range('list1', 1, 2)
        with self.assertRaises(TypeError):
            remove_list_range([1, 2], 'leftrange', 'rigthrange')
        with self.assertRaises(TypeError):
            remove_list_range([1, 2], 1, 'rigthrange')
        with self.assertRaises(TypeError):
            remove_list_range([1, 2], 'leftrange', 1)
