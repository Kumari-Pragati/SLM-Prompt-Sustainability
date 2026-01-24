import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
        self.assertEqual(sort_sublists([[1], [2, 3, 4]]), [[1], [2, 3, 4]])

    def test_edge_conditions(self):
        self.assertEqual(sort_sublists([]), [])
        self.assertEqual(sort_sublists([[]]), [[]])

    def test_complex_cases(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5], [6]]), [[1, 2, 3], [4, 5], [6]])
        self.assertEqual(sort_sublists([[1], [2, 3], [4, 5, 6]]), [[1], [2, 3], [4, 5, 6]])
        self.assertEqual(sort_sublists([[], [1, 2, 3], [4, 5, 6]]), [[], [1, 2, 3], [4, 5, 6]])
