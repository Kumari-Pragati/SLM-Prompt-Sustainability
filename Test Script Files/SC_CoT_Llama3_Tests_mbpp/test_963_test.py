import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_positive_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 3))

    def test_zero_discriminant(self):
        self.assertEqual(discriminant_value(1, 0, 1), ("one solution", 0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("no real solution", -3))

    def test_zero_x(self):
        self.assertEqual(discriminant_value(0, 2, 3), ("one solution", 4))

    def test_zero_y(self):
        self.assertEqual(discriminant_value(1, 0, 3), ("no real solution", 0))

    def test_zero_z(self):
        self.assertEqual(discriminant_value(1, 2, 0), ("Two solutions", 4))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            discriminant_value("a", 2, 3)

    def test_non_numeric_x(self):
        with self.assertRaises(TypeError):
            discriminant_value("a", 2, 3)

    def test_non_numeric_y(self):
        with self.assertRaises(TypeError):
            discriminant_value(1, "b", 3)

    def test_non_numeric_z(self):
        with self.assertRaises(TypeError):
            discriminant_value(1, 2, "c")
