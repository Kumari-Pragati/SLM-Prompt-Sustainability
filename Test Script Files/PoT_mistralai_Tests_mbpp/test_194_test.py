import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 24)
        self.assertEqual(octal_To_Decimal(30), 36)
        self.assertEqual(octal_To_Decimal(40), 52)
        self.assertEqual(octal_To_Decimal(50), 60)
        self.assertEqual(octal_To_Decimal(60), 72)
        self.assertEqual(octal_To_Decimal(70), 80)
        self.assertEqual(octal_To_Decimal(77), 95)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(1), 1)
        self.assertEqual(octal_To_Decimal(2), 2)
        self.assertEqual(octal_To_Decimal(3), 3)
        self.assertEqual(octal_To_Decimal(4), 4)
        self.assertEqual(octal_To_Decimal(5), 5)
        self.assertEqual(octal_To_Decimal(6), 6)
        self.assertEqual(octal_To_Decimal(7), 7)
        self.assertEqual(octal_To_Decimal(8), 8)
        self.assertEqual(octal_To_Decimal(9), 9)
        self.assertEqual(octal_To_Decimal(100), 80)
        self.assertEqual(octal_To_Decimal(1000), 8 * 100 + 0)
        self.assertEqual(octal_To_Decimal(10000), 8 * 1000 + 0)
        self.assertEqual(octal_To_Decimal(100000), 8 * 10000 + 0)
        self.assertEqual(octal_To_Decimal(1000000), 8 * 100000 + 0)
        self.assertEqual(octal_To_Decimal(10000000), 8 * 1000000 + 0)
        self.assertEqual(octal_To_Decimal(100000000), 8 * 10000000 + 0)
        self.assertEqual(octal_To_Decimal(1000000000), 8 * 100000000 + 0)
