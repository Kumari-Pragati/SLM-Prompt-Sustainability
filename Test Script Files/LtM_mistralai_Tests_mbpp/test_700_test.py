import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)
        self.assertEqual(count_range_in_list([-1, 0, 1, 2, 3], -1, 3), 4)
        self.assertEqual(count_range_in_list([0, 0, 1, 0, 0], 0, 1), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 0, 5), 0)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 6, 6), 0)
        self.assertEqual(count_range_in_list([-1, 0, 1, 2, 3], -2, -1), 0)
        self.assertEqual(count_range_in_list([-1, 0, 1, 2, 3], 4, 5), 0)

    def test_complex(self):
        self.assertEqual(count_range_in_list([-1, 0, 1, 2, 3, -1], -1, 3), 3)
        self.assertEqual(count_range_in_list([0, 0, 1, 0, 0, 1], 0, 1), 3)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6], 1, 6), 6)
