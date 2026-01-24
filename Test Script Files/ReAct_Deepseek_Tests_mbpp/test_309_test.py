import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(maximum(5, 10), 10)
        self.assertEqual(maximum(-5, -10), -5)
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(maximum(float('inf'), 10), float('inf'))
        self.assertEqual(maximum(-float('inf'), -10), -10)
        self.assertEqual(maximum(float('nan'), 10), float('nan'))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            maximum("5", 10)
        with self.assertRaises(TypeError):
            maximum(5, "10")
        with self.assertRaises(TypeError):
            maximum("5", "10")
