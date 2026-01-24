import unittest
from mbpp_544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):

    def test_flatten_tuple_normal(self):
        self.assertEqual(flatten_tuple([(1, 2), (3, 4), (5, 6)]), '1 2 3 4 5 6')

    def test_flatten_tuple_empty_list(self):
        self.assertEqual(flatten_tuple([]), '')

    def test_flatten_tuple_single_element(self):
        self.assertEqual(flatten_tuple([(1,)]), '1')

    def test_flatten_tuple_single_tuple(self):
        self.assertEqual(flatten_tuple([(1, 2)]), '1 2')

    def test_flatten_tuple_mixed_types(self):
        self.assertEqual(flatten_tuple([(1, 2), 'a', 3]), '1 2 a 3')

    def test_flatten_tuple_nested_tuples(self):
        self.assertEqual(flatten_tuple([(1, (2, 3)), (4, 5)]), '1 2 3 4 5')

    def test_flatten_tuple_empty_tuple(self):
        self.assertEqual(flatten_tuple([(), (1,)]), '1')
