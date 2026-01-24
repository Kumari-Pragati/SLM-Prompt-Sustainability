import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_simple_input(self):
        tri = [[1], [2, 3], [1, 5, 9]]
        n = 3
        self.assertEqual(max_sum(tri, n), 15)

    def test_edge_conditions(self):
        # Test with n = 1
        tri = [[1]]
        n = 1
        self.assertEqual(max_sum(tri, n), 1)

        # Test with n = 0
        tri = []
        n = 0
        self.assertEqual(max_sum(tri, n), 0)

    def test_complex_input(self):
        tri = [[1], [2, 4], [5, 1, 3], [3, 2, 4, 5]]
        n = 4
        self.assertEqual(max_sum(tri, n), 15)

    def test_invalid_input(self):
        # Test with negative numbers
        tri = [[1], [2, -4], [5, 1, 3], [3, 2, 4, 5]]
        n = 4
        self.assertEqual(max_sum(tri, n), 15)

        # Test with non-integer numbers
        tri = [[1], [2, 4.5], [5, 1, 3], [3, 2, 4, 5]]
        n = 4
        self.assertEqual(max_sum(tri, n), 15)
