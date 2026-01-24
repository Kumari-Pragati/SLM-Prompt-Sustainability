import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sort_sublists([[2, 1], [3, 4, 5]]), [[1, 2], [3, 4, 5]])
        self.assertEqual(sort_sublists([[10, 9, 8], [7, 6, 5, 4]]), [[8, 9, 10], [4, 5, 6, 7]])

    def test_edge_conditions(self):
        self.assertEqual(sort_sublists([[], []]), [[], []])
        self.assertEqual(sort_sublists([[], [1, 2, 3]]), [[], [1, 2, 3]])
        self.assertEqual(sort_sublists([[1, 2, 3], []]), [[1, 2, 3], []])

    def test_boundary_conditions(self):
        self.assertEqual(sort_sublists([[1], [1]]), [[1], [1]])
        self.assertEqual(sort_sublists([[1, 2, 3], [3, 2, 1]]), [[1, 2, 3], [1, 2, 3]])
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_complex_cases(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [3, 2, 1], [2, 3, 1]]), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        self.assertEqual(sort_sublists([[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 2, 3]]), [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
