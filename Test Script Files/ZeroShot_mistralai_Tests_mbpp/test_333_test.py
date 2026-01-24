import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_sort_single_element(self):
        self.assertEqual(Sort([(1, 'a'), (2, 'b'), (3, 'c')]), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_sort_multiple_elements(self):
        self.assertEqual(Sort([(2, 'b'), (1, 'a'), (3, 'c')]), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_sort_duplicate_elements(self):
        self.assertEqual(Sort([(2, 'b'), (2, 'b'), (1, 'a'), (3, 'c')]), [(1, 'a'), (2, 'b'), (2, 'b'), (3, 'c')])

    def test_sort_negative_numbers(self):
        self.assertEqual(Sort([(-2, 'b'), (-1, 'a'), (0, 'c'), (1, 'd'), (2, 'e')]), [(-2, 'b'), (-1, 'a'), (0, 'c'), (1, 'd'), (2, 'e')])
