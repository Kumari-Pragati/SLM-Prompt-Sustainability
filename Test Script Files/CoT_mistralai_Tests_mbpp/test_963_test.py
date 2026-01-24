import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 13))
        self.assertEqual(discriminant_value(4, 16, 36), ("Two solutions", 64))
        self.assertEqual(discriminant_value(9, 25, 4), ("Two solutions", 0))

    def test_zero_discriminant(self):
        self.assertEqual(discriminant_value(1, 1, 1), ("one solution", 0))
        self.assertEqual(discriminant_value(4, 16, 64), ("one solution", 0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("no real solution", -13))
        self.assertEqual(discriminant_value(4, -16, 36), ("no real solution", -13))
        self.assertEqual(discriminant_value(9, -25, 4), ("no real solution", -204))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, discriminant_value, "x", 2, 3)
        self.assertRaises(TypeError, discriminant_value, 1, "y", 3)
        self.assertRaises(TypeError, discriminant_value, 1, 2, "z")
