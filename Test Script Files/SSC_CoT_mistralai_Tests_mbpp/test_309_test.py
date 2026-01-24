import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(-5, -3), -3)
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(maximum(2147483647, 0), 2147483647)
        self.assertEqual(maximum(-2147483648, -1), -2147483648)
        self.assertEqual(maximum(float('inf'), 0), float('inf'))
        self.assertEqual(maximum(0, float('-inf')), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum('a', 'b')
        with self.assertRaises(TypeError):
            maximum([1, 2, 3], 4)
