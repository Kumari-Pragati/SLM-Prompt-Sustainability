import unittest
from mbpp_696_code import map
from six.moves import zip
from collections import Iterable
from six import string_types

from 696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_zip_list_with_two_lists(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(zip_list(['a', 'b', 'c'], ['d', 'e', 'f']), ['ad', 'be', 'cf'])
        self.assertEqual(zip_list([1.1, 2.2, 3.3], [4.4, 5.5, 6.6]), [5.5, 7.7, 9.9])

    def test_zip_list_with_lists_of_different_lengths(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5]), [5, 7])
        self.assertEqual(zip_list(['a', 'b'], ['c', 'd', 'e']), ['ac', 'be'])
        self.assertEqual(zip_list([1.1, 2.2], [3.3, 4.4, 5.5]), [3.3, 7.7])

    def test_zip_list_with_empty_list(self):
        self.assertEqual(zip_list([], ['a', 'b', 'c']), [])
        self.assertEqual(zip_list(['a', 'b', 'c'], []), [])

    def test_zip_list_with_non_iterable_input(self):
        self.assertRaises(TypeError, zip_list, 1, 2)
        self.assertRaises(TypeError, zip_list, 'a', 1)
        self.assertRaises(TypeError, zip_list, 1.1, 2.2)

    def test_zip_list_with_mixed_types(self):
        self.assertRaises(TypeError, zip_list, [1, 'a'], [2, 'b'])
        self.assertRaises(TypeError, zip_list, [1, 2], ['a', 'b'])
