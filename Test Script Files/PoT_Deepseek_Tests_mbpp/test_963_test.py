import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(discriminant_value(1, 4, 1), ("one solution", 0))
        self.assertEqual(discriminant_value(1, 0, -4), ("Two solutions", 16))
        self.assertEqual(discriminant_value(1, -4, 4), ("no real solution", -16))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("no real solution", 0))
        self.assertEqual(discriminant_value(0, 0, 1), ("no real solution", -4))
        self.assertEqual(discriminant_value(0, 1, 0), ("one solution", 0))

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            discriminant_value("a", 1, 1)
        with self.assertRaises(TypeError):
            discriminant_value(1, "a", 1)
        with self.assertRaises(TypeError):
            discriminant_value(1, 1, "a")
