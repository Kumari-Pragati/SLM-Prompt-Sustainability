import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", 15))
        self.assertEqual(discriminant_value(-1, 2, 3), ("Two solutions", -15))
        self.assertEqual(discriminant_value(1, -2, 3), ("Two solutions", 15))
        self.assertEqual(discriminant_value(1, 2, -3), ("Two solutions", -15))

    def test_edge_and_boundary_cases(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("one solution", 0))
        self.assertEqual(discriminant_value(0, 1, 0), ("no real solution", -1))
        self.assertEqual(discriminant_value(1, 0, 0), ("no real solution", -4))
        self.assertEqual(discriminant_value(1, 1, 0), ("one solution", 0))
        self.assertEqual(discriminant_value(1, 1, 1), ("no real solution", -2))
