import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(discriminant_value(1, 2, 3), ("Two solutions", -7))

    def test_simple_zero(self):
        self.assertEqual(discriminant_value(1, 0, 1), ("one solution", 0))

    def test_simple_negative(self):
        self.assertEqual(discriminant_value(1, -2, 3), ("no real solution", 9))

    def test_edge_x_zero(self):
        self.assertEqual(discriminant_value(0, 2, 3), ("one solution", 4))

    def test_edge_y_zero(self):
        self.assertEqual(discriminant_value(1, 0, 0), ("no real solution", 0))

    def test_edge_z_zero(self):
        self.assertEqual(discriminant_value(1, 2, 0), ("Two solutions", 4))

    def test_edge_x_zero_y_zero(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("one solution", 0))

    def test_edge_x_zero_z_zero(self):
        self.assertEqual(discriminant_value(0, 2, 0), ("Two solutions", 4))

    def test_edge_y_zero_z_zero(self):
        self.assertEqual(discriminant_value(1, 0, 0), ("no real solution", 0))

    def test_edge_x_zero_y_zero_z_zero(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("one solution", 0))
