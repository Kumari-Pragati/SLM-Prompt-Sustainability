import unittest
from194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(octal_To_Decimal(''), 0)

    def test_single_digit(self):
        self.assertEqual(octal_To_Decimal('1'), 1)
        self.assertEqual(octal_To_Decimal('2'), 2)
        self.assertEqual(octal_To_Decimal('3'), 3)
        self.assertEqual(octal_To_Decimal('4'), 4)
        self.assertEqual(octal_To_Decimal('5'), 5)
        self.assertEqual(octal_To_Decimal('6'), 6)
        self.assertEqual(octal_To_Decimal('7'), 7)
        self.assertEqual(octal_To_Decimal('8'), 8)
        self.assertEqual(octal_To_Decimal('9'), 9)

    def test_multiple_digits(self):
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('11'), 9)
        self.assertEqual(octal_To_Decimal('12'), 10)
        self.assertEqual(octal_To_Decimal('13'), 11)
        self.assertEqual(octal_To_Decimal('14'), 12)
        self.assertEqual(octal_To_Decimal('15'), 13)
        self.assertEqual(octal_To_Decimal('16'), 14)
        self.assertEqual(octal_To_Decimal('17'), 15)
        self.assertEqual(octal_To_Decimal('20'), 16)
        self.assertEqual(octal_To_Decimal('21'), 17)
        self.assertEqual(octal_To_Decimal('22'), 18)
        self.assertEqual(octal_To_Decimal('23'), 19)
        self.assertEqual(octal_To_Decimal('24'), 20)
        self.assertEqual(octal_To_Decimal('25'), 21)
        self.assertEqual(octal_To_Decimal('26'), 22)
        self.assertEqual(octal_To_Decimal('27'), 23)
        self.assertEqual(octal_To_Decimal('30'), 24)
        self.assertEqual(octal_To_Decimal('31'), 25)
        self.assertEqual(octal_To_Decimal('32'), 26)
        self.assertEqual(octal_To_Decimal('33'), 27)
        self.assertEqual(octal_To_Decimal('34'), 28)
        self.assertEqual(octal_To_Decimal('35'), 29)
        self.assertEqual(octal_To_Decimal('36'), 30)
        self.assertEqual(octal_To_Decimal('37'), 31)

    def test_leading_zeros(self):
        self.assertEqual(octal_To_Decimal('010'), 8)
        self.assertEqual(octal_To_Decimal('011'), 9)
        self.assertEqual(octal_To_Decimal('012'), 10)
        self.assertEqual(octal_To_Decimal('013'), 11)
        self.assertEqual(octal_To_Decimal('014'), 12)
        self.assertEqual(octal_To_Decimal('015'), 13)
        self.assertEqual(octal_To_Decimal('016'), 14)
        self.assertEqual(octal_To_Decimal('017'), 15)
        self.assertEqual(octal_To_Decimal('020'), 16)
        self.assertEqual(octal_To_Decimal('021'), 17)
        self.assertEqual(octal_To_Decimal('022'), 18)
        self.assertEqual(octal_To_Decimal('023'), 19)
        self.assertEqual(octal