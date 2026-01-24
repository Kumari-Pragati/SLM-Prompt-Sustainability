import unittest
from mbpp_309_code import maximum

class TestMaximumFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(10, 8), 10)
        self.assertEqual(maximum(3, 2), 3)

    def test_edge_cases(self):
        self.assertEqual(maximum(5, 5), 5)
        self.assertEqual(maximum(-5, -8), -5)
        self.assertEqual(maximum(0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(maximum(1, 2), 2)
        self.assertEqual(maximum(-1, -2), -2)
        self.assertEqual(maximum(0, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum('a', 5)
        with self.assertRaises(TypeError):
            maximum(5, 'b')
