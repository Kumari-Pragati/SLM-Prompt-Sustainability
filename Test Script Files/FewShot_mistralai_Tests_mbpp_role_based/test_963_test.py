import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 4))
        self.assertEqual(discriminant_value(4, 16, 1), ("Two solutions", 121))

    def test_zero_discriminant(self):
        self.assertEqual(discriminant_value(1, 1, 1), ("one solution", 0))
        self.assertEqual(discriminant_value(-1, 1, 1), ("one solution", 0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, -2, 3), ("no real solution", -9))
        self.assertEqual(discriminant_value(-1, -2, 3), ("no real solution", -9))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, discriminant_value, 0, "string", 3)
        self.assertRaises(TypeError, discriminant_value, 1, 2, "list")
