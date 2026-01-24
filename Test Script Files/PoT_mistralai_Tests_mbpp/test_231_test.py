import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sum([[0, 3, 1], [4, 5, 6], [3, 8, 4]], 3), 12)
        self.assertEqual(max_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 18)

    def test_edge_case_small_triangle(self):
        self.assertEqual(max_sum([[1], [2]], 2), 3)

    def test_edge_case_single_row(self):
        self.assertEqual(max_sum([[1, 2, 3]], 1), 1)
        self.assertEqual(max_sum([[1, 2, 3]], 3), 3)

    def test_edge_case_single_column(self):
        self.assertEqual(max_sum([[1], [2], [3]], 1), 1)
        self.assertEqual(max_sum([[1], [2], [3]], 3), 3)

    def test_corner_case_empty_triangle(self):
        self.assertEqual(max_sum([], 0), 0)
