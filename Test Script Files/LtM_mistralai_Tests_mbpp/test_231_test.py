import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_sum([[1], [2, 3]], 2), 5)
        self.assertEqual(max_sum([[1, 2], [3, 4], [5, 6]], 3), 12)

    def test_edge_input(self):
        self.assertEqual(max_sum([], 1), 0)
        self.assertEqual(max_sum([[1]], 1), 1)
        self.assertEqual(max_sum([[1], [2]], 1), 2)
        self.assertEqual(max_sum([[1], [2], [3]], 0), 1)
        self.assertEqual(max_sum([[1], [2], [3]], 4), 3)

    def test_boundary_input(self):
        self.assertEqual(max_sum([[-100], [100]], 2), 200)
        self.assertEqual(max_sum([[100], [-100]], 2), 200)
        self.assertEqual(max_sum([[-100], [100]], 1), 100)
        self.assertEqual(max_sum([[100], [-100]], 1), -100)

    def test_complex_input(self):
        self.assertEqual(max_sum([[1, 2], [3, 4], [5, 6], [7, 8]], 4), 16)
        self.assertEqual(max_sum([[-1, -2], [3, 4], [-5, -6], [-7, -8]], 4), -8)
