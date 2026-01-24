import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(20), 24)
        self.assertEqual(decimal_to_Octal(100), 144)

    def test_edge_cases(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(64), 100)

    def test_boundary_cases(self):
        self.assertEqual(decimal_to_Octal(7), 7)
        self.assertEqual(decimal_to_Octal(511), 777)
        self.assertEqual(decimal_to_Octal(512), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal("10")
        with self.assertRaises(TypeError):
            decimal_to_Octal(-10)
        with self.assertRaises(TypeError):
            decimal_to_Octal(10.5)
