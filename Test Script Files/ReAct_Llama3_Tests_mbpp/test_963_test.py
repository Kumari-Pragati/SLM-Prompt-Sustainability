import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 3))

    def test_zero_discriminant(self):
        self.assertEqual(discriminant_value(1, 0, 1), ("one solution", 0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("no real solution", -3))

    def test_zero_coefficients(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("one solution", 0))

    def test_nonzero_coefficients(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            discriminant_value("a", 2, 3)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            discriminant_value(1, "b", 3)
