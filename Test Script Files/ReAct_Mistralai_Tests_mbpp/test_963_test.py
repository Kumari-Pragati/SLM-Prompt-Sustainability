import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_positive_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 15))
        self.assertEqual(discriminant_value(4, 2, 1), ("Two solutions", 16))
        self.assertEqual(discriminant_value(0, 2, -1), ("Two solutions", 4))

    def test_zero_discriminant(self):
        self.assertEqual(discriminant_value(1, 0, 1), ("one solution", 0))
        self.assertEqual(discriminant_value(4, 0, -16), ("one solution", 0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("no real solution", -15))
        self.assertEqual(discriminant_value(4, 2, -17), ("no real solution", -100))

    def test_invalid_input(self):
        self.assertRaises(TypeError, discriminant_value, "x", 2, 3)
        self.assertRaises(TypeError, discriminant_value, 1, "y", 3)
        self.assertRaises(TypeError, discriminant_value, 1, 2, "z")
