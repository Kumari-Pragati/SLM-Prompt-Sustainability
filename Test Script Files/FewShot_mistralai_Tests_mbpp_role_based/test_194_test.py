import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_valid_octal_numbers(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 16)
        self.assertEqual(octal_To_Decimal(30), 24)
        self.assertEqual(octal_To_Decimal(77), 63)

    def test_zero_and_one(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(1), 1)

    def test_edge_case_leading_zero(self):
        self.assertEqual(octal_To_Decimal(001), 1)
        self.assertEqual(octal_To_Decimal(007), 7)

    def test_edge_case_leading_zeros_and_digits(self):
        self.assertEqual(octal_To_Decimal(010), 8)
        self.assertEqual(octal_To_Decimal(077), 63)

    def test_invalid_input_non_octal(self):
        self.assertRaises(ValueError, octal_To_Decimal, 'a')

    def test_invalid_input_negative_number(self):
        self.assertRaises(ValueError, octal_To_Decimal, -1)
