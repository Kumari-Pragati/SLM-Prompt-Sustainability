import unittest

from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]), 
                         [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])

    def test_edge_case(self):
        self.assertEqual(sort_list_last([]), [])

    def test_corner_case(self):
        self.assertEqual(sort_list_last([(1, 1), (1, 1), (1, 1)]), 
                         [(1, 1), (1, 1), (1, 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list_last([1, 2, 3])
