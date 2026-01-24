import unittest
from mbpp_696_code import map
from collections import Iterable

from696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_zip_normal(self):
        self.assertListEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertListEqual(zip_list([], []), [])
        self.assertListEqual(zip_list([1], [2, 3]), [3])
        self.assertListEqual(zip_list([1, 2], []), [None, None])

    def test_zip_edge_cases(self):
        self.assertListEqual(zip_list([1, 2], [3, 4, 5]), [4, 5])
        self.assertListEqual(zip_list([1, 2, 3], [4]), [5])
        self.assertListEqual(zip_list([1, 2], [3, 4, 5, 6]), [5, None])
        self.assertListEqual(zip_list([1, 2, 3], [4, 5]), [5, 6])

    def test_zip_invalid_inputs(self):
        with self.assertRaises(TypeError):
            zip_list('abc', [1, 2, 3])
        with self.assertRaises(TypeError):
            zip_list([1, 2], 'abc')
        with self.assertRaises(TypeError):
            zip_list(1, [1, 2])
        with self.assertRaises(TypeError):
            zip_list([1, 2], 1)
