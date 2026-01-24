import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(max_sum([-1, -2, -3, -4], 4), 0)
        self.assertEqual(max_sum([0, 0, 0, 0], 4), 0)

    def test_edge_cases(self):
        self.assertEqual(max_sum([1], 1), 1)
        self.assertEqual(max_sum([1, 2], 2), 3)
        self.assertEqual(max_sum([1, 2, 3], 3), 6)
        self.assertEqual(max_sum([1, 2, 3, 4], 1), 5)
        self.assertEqual(max_sum([1, 2, 3, 4], 5), 10)
        self.assertEqual(max_sum([], 0), 0)

    def test_complex_cases(self):
        self.assertEqual(max_sum([1, 2, 3, -1, -2, -3], 6), 2)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5, -6], 6), -1)
        self.assertEqual(max_sum([100, 200, 300, 400, 500, 600], 6), 1500)
