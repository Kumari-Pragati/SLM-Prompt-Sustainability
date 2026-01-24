import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_octal_to_decimal(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 16)
        self.assertEqual(octal_To_Decimal(30), 24)
        self.assertEqual(octal_To_Decimal(100), 64)
        self.assertEqual(octal_To_Decimal(1000), 4096)
        self.assertEqual(octal_To_Decimal(1234), 668)
        self.assertEqual(octal_To_Decimal(7777), 4095)
        self.assertEqual(octal_To_Decimal(10000), 4096)
