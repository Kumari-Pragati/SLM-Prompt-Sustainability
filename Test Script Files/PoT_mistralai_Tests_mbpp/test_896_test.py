import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_sort_single_element_list(self):
        self.assertEqual(sort_list_last([(1, 2)]), [(1, 2)])

    def test_sort_two_element_list(self):
        self.assertEqual(sort_list_last([(2, 1), (1, 2)]), [(1, 2), (2, 1)])

    def test_sort_multiple_elements_list(self):
        self.assertEqual(sort_list_last([(3, 'a'), (1, 'z'), (2, 'b'), (1, 'y'), (3, 'c')]),
                         [(1, 'y'), (1, 'z'), (2, 'b'), (3, 'a'), (3, 'c')])

    def test_sort_list_with_duplicates(self):
        self.assertEqual(sort_list_last([(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]),
                         [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')])

    def test_sort_list_with_mixed_types(self):
        self.assertEqual(sort_list_last([(1, 'a'), (1, 2), (2, 'a'), (2, 1)]),
                         [(1, 2), (1, 'a'), (2, 1), (2, 'a')])
