import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (1, 2, 3, 4, 5)
        test_tup2 = ('a', 'b', 'c', 'd', 'e')
        self.assertEqual(zip_tuples(test_tup1, test_tup2), [(2, 'a'), (3, 'b'), (4, 'c'), (5, 'd'), (1, 'e')])

    def test_edge_case_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(zip_tuples(test_tup1, test_tup2), [])

    def test_edge_case_single_element_tuples(self):
        test_tup1 = (1,)
        test_tup2 = ('a',)
        self.assertEqual(zip_tuples(test_tup1, test_tup2), [(1, 'a')])

    def test_edge_case_tuples_of_different_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = ('a', 'b', 'c', 'd', 'e')
        self.assertEqual(zip_tuples(test_tup1, test_tup2), [(2, 'a'), (3, 'b'), (1, 'c'), (2, 'd'), (3, 'e')])
