import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(10, 5), 10)
        self.assertEqual(maximum(5, 10), 10)
        self.assertEqual(maximum(5, 5), 5)
        self.assertEqual(maximum(-5, -10), -5)
        self.assertEqual(maximum(-5, 5), -5)
        self.assertEqual(maximum(0, 0), 0)
        self.assertEqual(maximum(0, 10), 10)
        self.assertEqual(maximum(10, 0), 10)

    def test_edge_cases(self):
        self.assertEqual(maximum(10, float('-inf')), 10)
        self.assertEqual(maximum(float('-inf'), 5), 5)
        self.assertEqual(maximum(float('inf'), 5), float('inf'))
        self.assertEqual(maximum(5, float('inf')), float('inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum('a', 5)
        with self.assertRaises(TypeError):
            maximum(5, 'b')
