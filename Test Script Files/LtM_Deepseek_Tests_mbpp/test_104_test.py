import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_sublists([[2, 3], [1, 2]]), [[2, 3], [1, 2]])

    def test_edge_condition_empty_input(self):
        self.assertEqual(sort_sublists([]), [])

    def test_boundary_condition_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[1, 2]])

    def test_complex_condition_multiple_sublists(self):
        self.assertEqual(sort_sublists([[3, 2], [1, 4], [5, 1]]), [[1, 2], [3, 4], [5, 1]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_sublists(104_code)
