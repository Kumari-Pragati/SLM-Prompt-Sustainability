import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_normal(self):
        self.assertEqual(sort_tuple((('a', 1), ('b', 2), ('c', 3))), (('a', 1), ('b', 2), ('c', 3)))
        self.assertEqual(sort_tuple((('z', 10), ('y', 9), ('x', 8))), (('x', 8), ('y', 9), ('z', 10)))

    def test_sort_edge_cases(self):
        self.assertEqual(sort_tuple((('z', 10), ('y', 9), ('x', 8), ('a', 1))), (('a', 1), ('x', 8), ('y', 9), ('z', 10)))
        self.assertEqual(sort_tuple((('z', 10), ('y', 9), ('x', 8), ('a', 1), ('b', 2))), (('a', 1), ('b', 2), ('x', 8), ('y', 9), ('z', 10)))

    def test_sort_reverse(self):
        self.assertEqual(sort_tuple((('z', 10), ('y', 9), ('x', 8))), (('x', 8), ('y', 9), ('z', 10)))

    def test_sort_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_sort_single_item(self):
        self.assertEqual(sort_tuple(('a', 1)), (('a', 1)))

    def test_sort_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple(1)
        with self.assertRaises(TypeError):
            sort_tuple('abc')
        with self.assertRaises(TypeError):
            sort_tuple([('a', 1)])
