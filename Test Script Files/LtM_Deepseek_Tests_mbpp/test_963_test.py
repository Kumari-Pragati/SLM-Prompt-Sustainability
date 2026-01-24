import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_positive_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("Two solutions", 4))

    def test_zero_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 1), ("one solution", 0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("no real solution", -4))

    def test_zero_coefficients(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("no real solution", -4))

    def test_negative_coefficients(self):
        self.assertEqual(discriminant_value(-1, -2, -3), ("Two solutions", 4))

    def test_zero_x(self):
        self.assertEqual(discriminant_value(0, 2, 1), ("one solution", 0))

    def test_negative_x(self):
        self.assertEqual(discriminant_value(-1, 2, 1), ("Two solutions", 0))

    def test_negative_y(self):
        self.assertEqual(discriminant_value(1, -2, 1), ("Two solutions", 4))

    def test_negative_z(self):
        self.assertEqual(discriminant_value(1, 2, -1), ("Two solutions", 4))

    def test_zero_y(self):
        self.assertEqual(discriminant_value(1, 0, 1), ("no real solution", -2))

    def test_zero_z(self):
        self.assertEqual(discriminant_value(1, 2, 0), ("Two solutions", 0))
