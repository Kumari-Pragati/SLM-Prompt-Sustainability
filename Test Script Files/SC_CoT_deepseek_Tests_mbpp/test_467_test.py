import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decimal_to_Octal(10), 12)

    def test_boundary_case(self):
        self.assertEqual(decimal_to_Octal(0), 0)

    def test_edge_case(self):
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(64), 100)

    def test_special_case(self):
        self.assertEqual(decimal_to_Octal(255), 377)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal('10')
        with self.assertRaises(ValueError):
            decimal_to_Octal(-10)
