import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(maximum(1, 2), 2)
        self.assertEqual(maximum(10, 5), 10)
        self.assertEqual(maximum(-1, -2), -1)

    def test_edge_cases(self):
        self.assertEqual(maximum(0, 0), 0)
        self.assertEqual(maximum(-1, 0), 0)
        self.assertEqual(maximum(0, -1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(maximum(float('inf'), 1), float('inf'))
        self.assertEqual(maximum(-float('inf'), -1), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum(1, 'a')
        with self.assertRaises(TypeError):
            maximum('a', 1)
        with self.assertRaises(TypeError):
            maximum('a', 'b')
