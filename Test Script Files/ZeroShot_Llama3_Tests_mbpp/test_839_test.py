import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_tuple(self):
        self.assertEqual(sort_tuple((5, 2)), (2, 5))
        self.assertEqual(sort_tuple((5, 3, 2)), (2, 3, 5))
        self.assertEqual(sort_tuple((5, 1, 3, 2)), (1, 2, 3, 5))
        self.assertEqual(sort_tuple((5, 5, 5)), (5, 5, 5))
        self.assertEqual(sort_tuple((5, 2, 3, 1)), (1, 2, 3, 5))
        self.assertEqual(sort_tuple((5, 2, 1, 3)), (1, 2, 3, 5))
        self.assertEqual(sort_tuple((5, 2, 1, 4)), (1, 2, 4, 5))
        self.assertEqual(sort_tuple((5, 2, 3, 4)), (2, 3, 4, 5))
        self.assertEqual(sort_tuple((5, 1, 2, 3)), (1, 2, 3, 5))
        self.assertEqual(sort_tuple((5, 1, 3, 2)), (1, 2, 3, 5))

    def test_sort_tuple_empty(self):
        self.assertEqual(sort_tuple(()), ())

    def test_sort_tuple_single(self):
        self.assertEqual(sort_tuple((5,)), (5,))
