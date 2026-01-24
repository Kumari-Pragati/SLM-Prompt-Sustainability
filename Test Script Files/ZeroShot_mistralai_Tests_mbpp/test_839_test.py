import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_tuple_empty(self):
        self.assertEqual(sort_tuple([]), [])

    def test_sort_tuple_single_element(self):
        self.assertEqual(sort_tuple([(1, 2)]), [(1, 2)])

    def test_sort_tuple_multiple_elements(self):
        self.assertEqual(sort_tuple([(3, 1), (1, 2), (2, 3), (1, 1)]), [(1, 1), (1, 2), (2, 3), (3, 1)])

    def test_sort_tuple_duplicates(self):
        self.assertEqual(sort_tuple([(1, 2), (1, 2), (3, 1), (1, 1)]), [(1, 1), (1, 1), (1, 2), (3, 1)])

    def test_sort_tuple_mixed_types(self):
        self.assertEqual(sort_tuple([(1, 2), (3, 'a'), (2, 1)]), [(1, 2), (2, 1), (3, 'a')])
