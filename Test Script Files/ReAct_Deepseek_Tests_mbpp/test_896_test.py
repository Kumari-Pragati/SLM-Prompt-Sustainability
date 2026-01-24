import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]),
                         [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])

    def test_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single_element(self):
        self.assertEqual(sort_list_last([(1, 2)]), [(1, 2)])

    def test_same_last_elements(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 5), (4, 4), (2, 4), (2, 1)]),
                         [(2, 1), (1, 5), (2, 4), (4, 4), (2, 5)])

    def test_negative_numbers(self):
        self.assertEqual(sort_list_last([(2, -5), (1, -2), (4, -4), (2, -3), (2, -1)]),
                         [(2, -1), (1, -2), (2, -3), (4, -4), (2, -5)])

    def test_large_numbers(self):
        self.assertEqual(sort_list_last([(2, 1000), (1, 2000), (4, 3000), (2, 2000), (2, 1000)]),
                         [(2, 1000), (1, 2000), (2, 2000), (4, 3000), (2, 1000)])
