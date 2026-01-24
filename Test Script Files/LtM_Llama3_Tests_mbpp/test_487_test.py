import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sort_tuple(()), ())

    def test_single_element_input(self):
        self.assertEqual(sort_tuple((1,)), (1,))

    def test_sorted_input(self):
        self.assertEqual(sort_tuple((1, 2, 3)), (1, 2, 3))

    def test_unsorted_input(self):
        self.assertEqual(sort_tuple((3, 1, 2)), (1, 2, 3))

    def test_negative_numbers_input(self):
        self.assertEqual(sort_tuple((-1, 0, 1)), (-1, 0, 1))

    def test_duplicates_input(self):
        self.assertEqual(sort_tuple((1, 2, 2, 3)), (1, 2, 2, 3))

    def test_long_input(self):
        self.assertEqual(sort_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9)), (1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_edge_case_input(self):
        self.assertEqual(sort_tuple((1, 1, 1)), (1, 1, 1))
