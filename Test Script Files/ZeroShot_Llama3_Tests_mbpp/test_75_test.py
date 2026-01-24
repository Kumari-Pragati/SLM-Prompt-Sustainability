import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_find_tuples(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), '[(3, 6, 9)]')
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 2), '[(2, 4, 6)]')
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 5), '[]')
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1), '[(1, 2, 3), (4, 5, 6), (7, 8, 9)]')
        self.assertEqual(find_tuples([], 3), '[]')

    def test_find_tuples_empty_list(self):
        self.assertEqual(find_tuples([], 3), '[]')

    def test_find_tuples_single_element(self):
        self.assertEqual(find_tuples([(1,)], 1), '[(1,)]')

    def test_find_tuples_single_element_empty_list(self):
        self.assertEqual(find_tuples([], 1), '[]')
