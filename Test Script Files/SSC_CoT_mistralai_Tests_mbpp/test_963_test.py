import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 15))
        self.assertEqual(discriminant_value(-1, 2, -3), ("Two solutions", 15))
        self.assertEqual(discriminant_value(1, -2, 3), ("Two solutions", 15))
        self.assertEqual(discriminant_value(-1, -2, -3), ("Two solutions", 15))

    def test_edge_cases(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("one solution", 0))
        self.assertEqual(discriminant_value(0, 0, 1), ("no real solution", -1))
        self.assertEqual(discriminant_value(1, 0, 0), ("no real solution", -3))
        self.assertEqual(discriminant_value(-1, 0, 0), ("no real solution", -3))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, discriminant_value, "x", 2, 3)
        self.assertRaises(TypeError, discriminant_value, 1, "y", 3)
        self.assertRaises(TypeError, discriminant_value, 1, 2, "z")
