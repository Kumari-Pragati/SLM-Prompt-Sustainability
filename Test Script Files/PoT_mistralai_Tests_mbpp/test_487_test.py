import unittest
from mbpp_487_code import sort_tuple

class TestSortTuples(unittest.TestCase):

    def test_sort_simple_tuples(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a')))
        self.assertEqual(sort_tuple((2, 'b', 3)), ((2, 'b', 3)))
        self.assertEqual(sort_tuple((3, 'a', 2)), ((3, 'a', 2)))
        self.assertEqual(sort_tuple((1, 'z', 2)), ((1, 'z', 2)))
        self.assertEqual(sort_tuple((2, 'y', 1)), ((2, 'y', 1)))

    def test_sort_tuples_with_different_types(self):
        self.assertEqual(sort_tuple((1, 'a', 2)), ((1, 'a', 2)))
        self.assertEqual(sort_tuple((2, 1, 'a')), ((2, 1, 'a')))
        self.assertEqual(sort_tuple((1, 2, 'a')), ((1, 2, 'a')))

    def test_sort_tuples_with_same_last_element(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a')))
        self.assertEqual(sort_tuple((2, 'b')), ((2, 'b')))
        self.assertEqual(sort_tuple((3, 'c')), ((3, 'c')))
        self.assertEqual(sort_tuple((1, 'z')), ((1, 'z')))
        self.assertEqual(sort_tuple((2, 'y')), ((2, 'y')))

    def test_sort_tuples_with_same_last_and_first_elements(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a')))
        self.assertEqual(sort_tuple((2, 'b')), ((2, 'b')))
        self.assertEqual(sort_tuple((3, 'c')), ((3, 'c')))
        self.assertEqual(sort_tuple((1, 'z')), ((1, 'z')))
        self.assertEqual(sort_tuple((2, 'y')), ((2, 'y')))

    def test_sort_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_sort_single_element_tuple(self):
        self.assertEqual(sort_tuple((1,)), (1,))
        self.assertEqual(sort_tuple((2,)), (2,))
        self.assertEqual(sort_tuple((3,)), (3,))
        self.assertEqual(sort_tuple((10,)), (10,))
