import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('1'), 1)
        self.assertEqual(octal_To_Decimal('2'), 2)
        self.assertEqual(octal_To_Decimal('3'), 3)
        self.assertEqual(octal_To_Decimal('4'), 4)
        self.assertEqual(octal_To_Decimal('5'), 5)
        self.assertEqual(octal_To_Decimal('6'), 6)
        self.assertEqual(octal_To_Decimal('7'), 7)
        self.assertEqual(octal_To_Decimal('8'), 8)
        self.assertEqual(octal_To_Decimal('9'), 9)
        self.assertEqual(octal_To_Decimal('10'), 10)
        self.assertEqual(octal_To_Decimal('11'), 11)
        self.assertEqual(octal_To_Decimal('12'), 12)
        self.assertEqual(octal_To_Decimal('13'), 13)
        self.assertEqual(octal_To_Decimal('14'), 14)
        self.assertEqual(octal_To_Decimal('15'), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(octal_To_Decimal(''), None)
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('1'), 1)
        self.assertEqual(octal_To_Decimal('123'), 123)
        self.assertEqual(octal_To_Decimal('123456'), 123456)
        self.assertEqual(octal_To_Decimal('123456789'), 123456789)

    def test_complex_and_corner_cases(self):
        self.assertEqual(octal_To_Decimal('100'), 64)
        self.assertEqual(octal_To_Decimal('123456789012'), 123456789012)
        self.assertEqual(octal_To_Decimal('123456789012345'), 123456789012345)
        self.assertEqual(octal_To_Decimal('1234567890123456789'), 1234567890123456789)
