import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_valid_octal_numbers(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('1'), 1)
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('12'), 10)
        self.assertEqual(octal_To_Decimal('123'), 83)

    def test_octal_numbers_with_leading_zeros(self):
        self.assertEqual(octal_To_Decimal('012'), 10)
        self.assertEqual(octal_To_Decimal('0123'), 83)

    def test_octal_numbers_with_multiple_digits(self):
        self.assertEqual(octal_To_Decimal('1234'), 668)
        self.assertEqual(octal_To_Decimal('12345'), 5353)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal('abc')
        with self.assertRaises(TypeError):
            octal_To_Decimal(123)

    def test_edge_cases(self):
        self.assertEqual(octal_To_Decimal(''), 0)
        self.assertEqual(octal_To_Decimal('0'), 0)
