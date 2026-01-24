import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(-5, -3), -3)
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(maximum(float('-inf'), 0), 0)
        self.assertEqual(maximum(0, float('inf')), float('inf'))
        self.assertEqual(maximum(float('nan'), 0), 0)
        self.assertEqual(maximum(0, float('nan')), float('nan'))
