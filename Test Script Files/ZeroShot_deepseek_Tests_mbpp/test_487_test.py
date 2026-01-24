import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_tuple(self):
        self.assertEqual(sort_tuple((('a', 2), ('b', 1), ('c', 3))), (('b', 1), ('a', 2), ('c', 3)))
        self.assertEqual(sort_tuple((('x', 5), ('y', 0), ('z', -1))), (('z', -1), ('y', 0), ('x', 5)))
        self.assertEqual(sort_tuple((('p', 10), ('q', 10), ('r', 10))), (('p', 10), ('q', 10), ('r', 10)))
        self.assertEqual(sort_tuple(()), ())
