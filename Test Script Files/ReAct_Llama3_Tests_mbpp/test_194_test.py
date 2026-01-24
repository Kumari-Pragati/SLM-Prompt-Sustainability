import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_octal_to_decimal_typical(self):
        self.assertEqual(octal_To_Decimal('12'), 10)

    def test_octal_to_decimal_edge(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('1'), 1)
        self.assertEqual(octal_To_Decimal('7'), 7)
        self.assertEqual(octal_To_Decimal('8'), 8)
        self.assertEqual(octal_To_Decimal('9'), 9)
        self.assertEqual(octal_To_Decimal('10'), 10)
        self.assertEqual(octal_To_Decimal('11'), 11)
        self.assertEqual(octal_To_Decimal('12'), 10)
        self.assertEqual(octal_To_Decimal('13'), 13)
        self.assertEqual(octal_To_Decimal('14'), 14)
        self.assertEqual(octal_To_Decimal('15'), 15)
        self.assertEqual(octal_To_Decimal('16'), 16)

    def test_octal_to_decimal_invalid_input(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal('a')
        with self.assertRaises(TypeError):
            octal_To_Decimal('abc')
        with self.assertRaises(TypeError):
            octal_To_Decimal('123abc')
