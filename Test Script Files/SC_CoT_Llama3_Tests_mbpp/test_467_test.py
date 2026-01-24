import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(15), 17)
        self.assertEqual(decimal_to_Octal(20), 22)

    def test_edge_cases(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(1), 1)
        self.assertEqual(decimal_to_Octal(8), 10)

    def test_boundary_cases(self):
        self.assertEqual(decimal_to_Octal(9), 10)
        self.assertEqual(decimal_to_Octal(16), 20)
        self.assertEqual(decimal_to_Octal(24), 30)

    def test_special_cases(self):
        self.assertEqual(decimal_to_Octal(255), 377)
        self.assertEqual(decimal_to_Octal(256), 1000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_to_Octal('a')
        with self.assertRaises(TypeError):
            decimal_to_Octal(None)
