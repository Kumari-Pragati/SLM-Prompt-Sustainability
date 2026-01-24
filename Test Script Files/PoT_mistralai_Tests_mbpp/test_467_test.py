import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(255), 377
        self.assertEqual(decimal_to_Octal(12345), 21413

    def test_edge_and_boundary_cases(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(7), 7)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(255), 377)
        self.assertEqual(decimal_to_Octal(256), 400)
