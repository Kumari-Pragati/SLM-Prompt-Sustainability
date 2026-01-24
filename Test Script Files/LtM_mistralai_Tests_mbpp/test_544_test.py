import unittest
from mbpp_544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(flatten_tuple([(1, 2), (3, 4)]), '1 2 3 4')

    def test_empty_input(self):
        self.assertEqual(flatten_tuple([]), '')

    def test_single_element_input(self):
        self.assertEqual(flatten_tuple([(1,)]), '1')

    def test_single_element_list(self):
        self.assertEqual(flatten_tuple([1]), '1')

    def test_mixed_input(self):
        self.assertEqual(flatten_tuple([(1, 2), 3, (4, 5)]), '1 2 3 4 5')

    def test_nested_tuples(self):
        self.assertEqual(flatten_tuple([(1, (2, 3)), (4, 5)]), '1 2 3 4 5')

    def test_negative_numbers(self):
        self.assertEqual(flatten_tuple([(-1, 2), (3, -4)]), '-1 2 3 -4')
