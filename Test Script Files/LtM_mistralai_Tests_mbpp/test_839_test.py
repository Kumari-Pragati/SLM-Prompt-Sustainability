import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_simple_sort(self):
        self.assertEqual(sort_tuple([(1, 2), (3, 4), (2, 1)]), [(1, 2), (2, 1), (3, 4)])
        self.assertEqual(sort_tuple([(5, 3), (2, 1), (4, 6)]), [(2, 1), (4, 6), (5, 3)])

    def test_edge_cases(self):
        self.assertEqual(sort_tuple([]), [])
        self.assertEqual(sort_tuple([(0, 0)]), [(0, 0)])
        self.assertEqual(sort_tuple([(1000000000, 1)]), [(1, 1000000000)])

    def test_complex_sort(self):
        self.assertEqual(sort_tuple([(1000000000, 1), (1, 1000000000)]), [(1, 1000000000), (1000000000, 1)])
        self.assertEqual(sort_tuple([(1, 2), (2, -1), (3, 4), (-1, 0)]), [(-1, 0), (1, 2), (2, -1), (3, 4)])
