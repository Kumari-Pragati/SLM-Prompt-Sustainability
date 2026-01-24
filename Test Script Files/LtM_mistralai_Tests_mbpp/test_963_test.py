import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 15))

    def test_simple_zero(self):
        self.assertEqual(discriminant_value(1, 0, 1), ("one solution", 0))

    def test_simple_negative(self):
        self.assertEqual(discriminant_value(1, -2, 1), ("no real solution", -3))

    def test_edge_zero_coefficients(self):
        self.assertEqual(discriminant_value(0, 0, 1), ("one solution", 0))
        self.assertEqual(discriminant_value(0, 1, 0), ("one solution", 0))
        self.assertEqual(discriminant_value(0, 0, 0), ("one solution", 0))

    def test_edge_negative_coefficients(self):
        self.assertEqual(discriminant_value(-1, -2, -3), ("no real solution", 37))

    def test_complex_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("no real solution", -21))

    def test_invalid_input_zero_x(self):
        with self.assertRaises(ValueError):
            discriminant_value(0, 2, 3)

    def test_invalid_input_zero_y(self):
        with self.assertRaises(ValueError):
            discriminant_value(1, 0, 3)

    def test_invalid_input_zero_z(self):
        with self.assertRaises(ValueError):
            discriminant_value(1, 2, 0)
