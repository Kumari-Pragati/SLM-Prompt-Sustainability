import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(20), 24)
        self.assertEqual(decimal_to_Octal(8), 10)

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(64), 100)

    def test_edge_conditions(self):
        self.assertEqual(decimal_to_Octal(7), 7)
        self.assertEqual(decimal_to_Octal(512), 1000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal('10')
        with self.assertRaises(ValueError):
            decimal_to_Octal(-10)
