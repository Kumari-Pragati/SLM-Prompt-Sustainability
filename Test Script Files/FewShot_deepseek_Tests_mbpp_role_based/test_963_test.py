import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):
    def test_two_solutions(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("Two solutions", 16))

    def test_one_solution(self):
        self.assertEqual(discriminant_value(1, 2, 1), ("one solution", 0))

    def test_no_real_solution(self):
        self.assertEqual(discriminant_value(1, 1, 2), ("no real solution", -3))

    def test_negative_x(self):
        self.assertEqual(discriminant_value(-1, 2, -3), ("Two solutions", 16))

    def test_zero_y(self):
        self.assertEqual(discriminant_value(1, 0, -3), ("Two solutions", 12))

    def test_zero_z(self):
        self.assertEqual(discriminant_value(1, 2, 0), ("Two solutions", 4))

    def test_zero_x_y_z(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("no real solution", -0))

    def test_negative_discriminant(self):
        self.assertEqual(discriminant_value(1, -2, 1), ("Two solutions", -4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            discriminant_value("a", 2, 1)
