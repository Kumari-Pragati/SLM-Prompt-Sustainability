import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(diff_even_odd([1, 2, 3, 4]), 2)
        self.assertEqual(diff_even_odd([10, 15, 20, 25]), 10)
        self.assertEqual(diff_even_odd([-1, -2, -3, -4]), -2)
        self.assertEqual(diff_even_odd([0, 1, 2, 3]), 2)

    def test_edge_cases(self):
        self.assertEqual(diff_even_odd([1]), -1)
        self.assertEqual(diff_even_odd([2]), -1)
        self.assertEqual(diff_even_odd([1, 3, 5]), -1)
        self.assertEqual(diff_even_odd([2, 4, 6]), -1)

    def test_corner_cases(self):
        self.assertEqual(diff_even_odd([]), -1)
        self.assertEqual(diff_even_odd([1, 1, 1, 1]), -1)
        self.assertEqual(diff_even_odd([2, 2, 2, 2]), -1)
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), -1)
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), -1)
