import unittest
from mbpp_444_code import List, Tuple

from 444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(trim_tuple([], 0), "[]")

    def test_single_element_list(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 1), "[(2, 3)]")

    def test_list_with_single_element(self):
        self.assertEqual(trim_tuple([(1,)], 0), "[]")
        self.assertEqual(trim_tuple([(1,)], 1), "[(1)]")

    def test_list_with_multiple_elements(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1), "[(2, 3), (5, 6), (8, 9)]")

    def test_list_with_odd_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5), (6, 7, 8)], 1), "[(2, 3), (5,), (7, 8)]")

    def test_list_with_even_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6), (7, 8)], 1), "[(2, 3), (5, 6), (8,)]")
