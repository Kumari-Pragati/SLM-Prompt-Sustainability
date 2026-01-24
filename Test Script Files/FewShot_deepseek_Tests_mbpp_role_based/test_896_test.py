import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]),
                         [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])

    def test_edge_condition(self):
        self.assertEqual(sort_list_last([(1, 1), (1, 1)]),
                         [(1, 1), (1, 1)])

    def test_boundary_condition(self):
        self.assertEqual(sort_list_last([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
                         [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list_last(123)

        with self.assertRaises(TypeError):
            sort_list_last([1, 2, 3])

        with self.assertRaises(TypeError):
            sort_list_last('string')
