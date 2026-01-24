import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(-2, -5), -2)
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(maximum(float('-inf'), 0), float('-inf'))
        self.assertEqual(maximum(0, float('inf')), float('inf'))
        self.assertEqual(maximum(float('nan'), 0), float('nan'))
        self.assertEqual(maximum(0, float('nan')), 0)

    def test_complex(self):
        self.assertEqual(maximum(-5, 3.14), 3.14)
        self.assertEqual(maximum(3.14, -5), 3.14)
        self.assertEqual(maximum(-5, -3.14), -5)
        self.assertEqual(maximum(-3.14, -5), -5)
