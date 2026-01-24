import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_octal_to_decimal(self):
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('12'), 10)
        self.assertEqual(octal_To_Decimal('123'), 83)
        self.assertEqual(octal_To_Decimal('1234'), 668)
        self.assertEqual(octal_To_Decimal('12345'), 5349)
        self.assertEqual(octal_To_Decimal('123456'), 42157)
        self.assertEqual(octal_To_Decimal('1234567'), 368515)
        self.assertEqual(octal_To_Decimal('12345678'), 2999998)
        self.assertEqual(octal_To_Decimal('123456789'), 24310567)
        self.assertEqual(octal_To_Decimal('1234567890'), 199999998)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal('a')
        with self.assertRaises(TypeError):
            octal_To_Decimal('123abc')
        with self.assertRaises(TypeError):
            octal_To_Decimal('1234567890x')

    def test_edge_cases(self):
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
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('11'), 9)
        self.assertEqual(octal_To_Decimal('12'), 10)
        self.assertEqual(octal_To_Decimal('13'), 11)
        self.assertEqual(octal_To_Decimal('14'), 12)
        self.assertEqual(octal_To_Decimal('15'), 13)
        self.assertEqual(octal_To_Decimal('16'), 14)
        self.assertEqual(octal_To_Decimal('17'), 15)
        self.assertEqual(octal_To_Decimal('18'), 16)
        self.assertEqual(octal_To_Decimal('19'), 17)
        self.assertEqual(octal_To_Decimal('20'), 18)
