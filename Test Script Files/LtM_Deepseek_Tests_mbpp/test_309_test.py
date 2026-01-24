import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(maximum(1, 2), 2)
        self.assertEqual(maximum(3, 1), 3)
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(maximum(-1, -2), -1)
        self.assertEqual(maximum(float('-inf'), float('inf')), float('inf'))

    def test_boundary_conditions(self):
        self.assertEqual(maximum(float('inf'), float('inf')), float('inf'))
        self.assertEqual(maximum(float('-inf'), float('-inf')), float('-inf'))

    def test_complex_cases(self):
        self.assertEqual(maximum(1.5, 1.49), 1.5)
        self.assertEqual(maximum(float('nan'), 1), 1)
        self.assertEqual(maximum(float('nan'), float('nan')), float('nan'))
