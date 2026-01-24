import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(5, 5, 5), 5)

    def test_edge_conditions(self):
        self.assertEqual(median_numbers(0, 0, 0), 0)
        self.assertEqual(median_numbers(1, 2, float('inf')), 2)
        self.assertEqual(median_numbers(float('-inf'), float('inf'), 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(median_numbers(1, 2, float('nan')), float('nan'))
        self.assertEqual(median_numbers(float('inf'), float('inf'), float('inf')), float('inf'))
        self.assertEqual(median_numbers(float('-inf'), float('-inf'), float('-inf')), float('-inf'))

    def test_complex_cases(self):
        self.assertEqual(median_numbers(10, 20, 15), 15)
        self.assertEqual(median_numbers(25, 25, 30), 25)
        self.assertEqual(median_numbers(float('nan'), 2, 3), 2)
        self.assertEqual(median_numbers(float('inf'), float('inf'), float('-inf')), float('inf'))
