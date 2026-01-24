import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum(5, 10), 10)
        self.assertEqual(maximum(15, 5), 15)
        self.assertEqual(maximum(10, 10), 10)

    def test_negative_numbers(self):
        self.assertEqual(maximum(-5, -10), -5)
        self.assertEqual(maximum(-15, -5), -5)
        self.assertEqual(maximum(-10, -10), -10)

    def test_boundary_conditions(self):
        self.assertEqual(maximum(0, -1), 0)
        self.assertEqual(maximum(-1, 0), 0)
        self.assertEqual(maximum(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum("5", 10)
        with self.assertRaises(TypeError):
            maximum(5, "10")
        with self.assertRaises(TypeError):
            maximum("5", "10")
