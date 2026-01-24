import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3)]),
                         [(2, 3), (1, 2), (4, 4), (2, 5)])

    def test_edge_conditions(self):
        self.assertEqual(sort_list_last([]), [])
        self.assertEqual(sort_list_last([(1, 2)]), [(1, 2)])

    def test_complex_cases(self):
        self.assertEqual(sort_list_last([(1, 2), (1, 3), (1, 1)]),
                         [(1, 1), (1, 2), (1, 3)])
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3)]),
                         [(2, 3), (1, 2), (4, 4), (2, 5)])
