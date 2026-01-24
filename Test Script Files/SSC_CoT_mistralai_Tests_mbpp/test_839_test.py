import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_normal(self):
        self.assertEqual(sort_tuple([(1, 2), (3, 4), (2, 1)]), [(1, 2), (2, 1), (3, 4)])
        self.assertEqual(sort_tuple([(5, 6), (4, 3), (2, 1)]), [(2, 1), (4, 3), (5, 6)])

    def test_sort_edge_cases(self):
        self.assertEqual(sort_tuple([(1, 2), (1, 3)]), [(1, 2), (1, 3)])
        self.assertEqual(sort_tuple([(1, 2), (2, 1), (1, 2)]), [(1, 2), (2, 1), (1, 2)])
        self.assertEqual(sort_tuple([(1, 2), (2, 1), (1, 2), (2, 1)]), [(1, 2), (2, 1), (1, 2), (2, 1)])

    def test_sort_empty_tuple(self):
        self.assertEqual(sort_tuple([]), [])

    def test_sort_single_element_tuple(self):
        self.assertEqual(sort_tuple([(1, 2)]), [(1, 2)])

    def test_sort_negative_numbers(self):
        self.assertEqual(sort_tuple([(-1, 2), (3, -2), (-3, 4)]), [(-3, 4), (-1, 2), (3, -2)])

    def test_sort_tuples_with_same_first_element(self):
        self.assertEqual(sort_tuple([(1, 2), (1, 3)]), [(1, 2), (1, 3)])
        self.assertEqual(sort_tuple([(1, 2), (1, 2), (1, 3)]), [(1, 2), (1, 2), (1, 3)])
