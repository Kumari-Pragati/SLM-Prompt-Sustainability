import unittest
from mbpp_544_code import List, Tuple

from 544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_tuple([]), '')

    def test_single_element_list(self):
        self.assertEqual(flatten_tuple([(1, 2, 3)]), '1 2 3')

    def test_multiple_elements_list(self):
        self.assertEqual(flatten_tuple([(1, 2), (3, 4), (5, 6, 7)]), '1 2 3 4 5 6 7')

    def test_mixed_types_list(self):
        self.assertEqual(flatten_tuple([(1, 2), ('a', 'b'), (3, 4, 5)]), '1 2 a b 3 4 5')

    def test_nested_tuples(self):
        self.assertEqual(flatten_tuple([(1, (2, 3)), (4, (5, 6))]), '1 2 3 4 5 6')
