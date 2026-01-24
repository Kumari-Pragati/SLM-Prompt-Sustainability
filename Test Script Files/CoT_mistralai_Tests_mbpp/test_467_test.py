import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(decimal_to_Octal(10), "22")
        self.assertEqual(decimal_to_Octal(100), "144")
        self.assertEqual(decimal_to_Octal(1000), "1600")
        self.assertEqual(decimal_to_Octal(10000), "12500")

    def test_zero(self):
        self.assertEqual(decimal_to_Octal(0), "0")

    def test_negative_numbers(self):
        self.assertEqual(decimal_to_Octal(-1), "377")
        self.assertEqual(decimal_to_Octal(-10), "7777")
        self.assertEqual(decimal_to_Octal(-100), "177777")
        self.assertEqual(decimal_to_Octal(-1000), "3777777")

    def test_large_numbers(self):
        self.assertEqual(decimal_to_Octal(18446744073709551615), "4503599627370495")

    def test_edge_cases(self):
        self.assertEqual(decimal_to_Octal(1), "1")
        self.assertEqual(decimal_to_Octal(8), "8")
        self.assertEqual(decimal_to_Octal(255), "377")
        self.assertEqual(decimal_to_Octal(377), "377")
        self.assertEqual(decimal_to_Octal(1023), "1307")
        self.assertEqual(decimal_to_Octal(1024), "2000")
        self.assertEqual(decimal_to_Octal(18446744073709551615), "4503599627370495")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, decimal_to_Octal, "string")
        self.assertRaises(TypeError, decimal_to_Octal, 0.0)
        self.assertRaises(TypeError, decimal_to_Octal, -1.0)
        self.assertRaises(TypeError, decimal_to_Octal, complex(0, 0))
