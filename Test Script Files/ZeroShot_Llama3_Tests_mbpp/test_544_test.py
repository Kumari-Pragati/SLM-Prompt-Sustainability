import unittest
from mbpp_544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):

    def test_flatten_tuple(self):
        self.assertEqual(flatten_tuple([(1, 2), (3, 4)]), '1 2 3 4')
        self.assertEqual(flatten_tuple([(1, 2, 3), (4, 5, 6)]), '1 2 3 4 5 6')
        self.assertEqual(flatten_tuple([(1, 2), (3, 4), (5, 6, 7)]), '1 2 3 4 5 6 7')
        self.assertEqual(flatten_tuple([(1, 2, 3, 4), (5, 6, 7, 8)]), '1 2 3 4 5 6 7 8')
        self.assertEqual(flatten_tuple([]), '')
        self.assertEqual(flatten_tuple([(1,)]), '1')
        self.assertEqual(flatten_tuple([(1, 2)]), '1 2')
        self.assertEqual(flatten_tuple([(1, 2, 3)]), '1 2 3')

    def test_flatten_tuple_empty(self):
        self.assertEqual(flatten_tuple([]), '')
