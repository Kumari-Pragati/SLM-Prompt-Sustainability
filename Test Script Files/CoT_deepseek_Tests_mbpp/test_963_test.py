import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_two_solutions(self):
        self.assertEqual(discriminant_value(1, 2, -3), ("Two solutions", 16))

    def test_one_solution(self):
        self.assertEqual(discriminant_value(1, -2, 1), ("one solution", 0))

    def test_no_real_solution(self):
        self.assertEqual(discriminant_value(1, 1, 1), ("no real solution", -3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            discriminant_value("a", 2, 3)

    def test_zero_coefficients(self):
        self.assertEqual(discriminant_value(0, 0, 0), ("no real solution", -0))

    def test_negative_coefficients(self):
        self.assertEqual(discriminant_value(-1, -2, -3), ("Two solutions", 16))
