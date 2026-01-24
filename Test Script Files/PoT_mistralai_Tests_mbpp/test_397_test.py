import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(2, 3, 1), 2)
        self.assertEqual(median_numbers(-1, -2, -3), -1.5)
        self.assertEqual(median_numbers(0, 0, 0), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(median_numbers(float('inf'), 2, 3), 2)
        self.assertEqual(median_numbers(2, float('inf'), 3), 2)
        self.assertEqual(median_numbers(2, 3, float('inf')), 2)
        self.assertEqual(median_numbers(-float('inf'), -2, -3), -2)
        self.assertEqual(median_numbers(-2, -float('inf'), -3), -2)
        self.assertEqual(median_numbers(-2, -3, -float('inf')), -2)
        self.assertEqual(median_numbers(1, 2, 3, 4), 2.5)
        self.assertEqual(median_numbers(1, 2, 3, 4, 5), 2.5)
        self.assertEqual(median_numbers(1, 2, 3, 4, 5, 6), 3)
        self.assertEqual(median_numbers(1, 2, 3, 4, 5, 6, 7), 3.5)
