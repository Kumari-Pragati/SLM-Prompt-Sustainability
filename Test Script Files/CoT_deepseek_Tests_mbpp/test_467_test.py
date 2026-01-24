import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decimal_to_Octal(10), 12)

    def test_zero(self):
        self.assertEqual(decimal_to_Octal(0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(64), 100)

    def test_large_numbers(self):
        self.assertEqual(decimal_to_Octal(255), 377)

    def test_negative_numbers(self):
        self.assertEqual(decimal_to_Octal(-10), -12)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal(10.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal('ten')
