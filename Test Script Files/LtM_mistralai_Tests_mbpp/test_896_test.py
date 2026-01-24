import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_simple_tuples(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6)]), [(5, 6), (3, 4), (1, 2)])
        self.assertEqual(sort_list_last([('a', 'b'), ('c', 'd'), ('e', 'f')]), [('e', 'f'), ('c', 'd'), ('a', 'b')])

    def test_edge_cases(self):
        self.assertEqual(sort_list_last([]), [])
        self.assertEqual(sort_list_last([(1,), (2,), (3,)]), [(3,), (2,), (1,)])
        self.assertEqual(sort_list_last([('a',), ('b',), ('c',)]), [('c',), ('b',), ('a',)])

    def test_complex_cases(self):
        self.assertEqual(sort_list_last([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [(9, 8, 7), (6, 5, 4), (3, 2, 1)])
        self.assertEqual(sort_list_last([('x', 'y', 'z'), ('a', 'b', 'c'), ('d', 'e', 'f')]), [('f', 'e', 'd'), ('c', 'b', 'a'), ('z', 'y', 'x')])
