import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(255), 377
        self.assertEqual(decimal_to_Octal(1024), 1000

    def test_edge_cases(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(7), 7)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(256), 377

    def test_boundary_conditions(self):
        self.assertEqual(decimal_to_Octal(7999), 21777
        self.assertEqual(decimal_to_Octal(20479), 53317
        self.assertEqual(decimal_to_Octal(65535), 1000000

    def test_negative_numbers(self):
        self.assertEqual(decimal_to_Octal(-1), 'Error: Negative numbers not supported' if '-1' not in str(SystemExit) else SystemExit(-1)
