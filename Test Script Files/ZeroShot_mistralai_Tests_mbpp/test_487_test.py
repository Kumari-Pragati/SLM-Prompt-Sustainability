import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(sort_tuple([]), [])

    def test_sort_single_element(self):
        self.assertEqual(sort_tuple([(1, 2)]), [(1, 2)])

    def test_sort_multiple_elements(self):
        self.assertEqual(sort_tuple([(3, 'z'), (1, 'a'), (2, 'b'), (4, 'd'), (0, 'c')]), [(0, 'c'), (1, 'a'), (2, 'b'), (3, 'z'), (4, 'd')])

    def test_sort_multiple_elements_with_duplicates(self):
        self.assertEqual(sort_tuple([(3, 'z'), (1, 'a'), (2, 'b'), (3, 'z'), (1, 'a')]), [(1, 'a'), (1, 'a'), (2, 'b'), (3, 'z'), (3, 'z')])

    def test_sort_multiple_elements_with_mixed_types(self):
        self.assertEqual(sort_tuple([(3, 'z'), (1, 2), (2, 'b'), (4, 5), (0, 'c')]), [(0, 'c'), (1, 2), (2, 'b'), (3, 4), (4, 5)])
