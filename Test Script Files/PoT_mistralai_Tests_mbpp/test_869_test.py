import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 3, 5), [(3, 4)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 2, 6), [(1, 2), (3, 4), (5, 6)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 1, 7), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_edge_case_min(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 0, 5), [])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], -1, 5), [])

    def test_edge_case_max(self):
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 3, 9), [(3, 4)])
        self.assertListEqual(remove_list_range([(1, 2), (3, 4), (5, 6), (7, 8)], 3, 10), [])

    def test_boundary_case_min(self):
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3), (4, 4)], 1, 1), [(1, 1)])
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3), (4, 4)], 0, 1), [])

    def test_boundary_case_max(self):
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3), (4, 4)], 1, 2), [(2, 2)])
        self.assertListEqual(remove_list_range([(1, 1), (2, 2), (3, 3), (4, 4)], 2, 3), [])
