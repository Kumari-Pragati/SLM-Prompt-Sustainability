import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_edge(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4)]), [(1, 2), (3, 4)])

    def test_edge2(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6), (7, 8)]), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_empty(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single(self):
        self.assertEqual(sort_list_last([(1, 2)]), [(1, 2)])

    def test_single2(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4)]), [(1, 2), (3, 4)])
