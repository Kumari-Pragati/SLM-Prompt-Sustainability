import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 24)
        self.assertEqual(octal_To_Decimal(30), 42)
        self.assertEqual(octal_To_Decimal(40), 56)
        self.assertEqual(octal_To_Decimal(50), 70)
        self.assertEqual(octal_To_Decimal(60), 84)
        self.assertEqual(octal_To_Decimal(70), 98)
        self.assertEqual(octal_To_Decimal(77), 121)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(1), 1)
        self.assertEqual(octal_To_Decimal(2), 2)
        self.assertEqual(octal_To_Decimal(3), 3)
        self.assertEqual(octal_To_Decimal(7), 7)
        self.assertEqual(octal_To_Decimal(8), 8)
        self.assertEqual(octal_To_Decimal(9), 9)
        self.assertEqual(octal_To_Decimal(100), 80)
        self.assertEqual(octal_To_Decimal(1000), 1024)
        self.assertEqual(octal_To_Decimal(10_000), 81920)
        self.assertEqual(octal_To_Decimal(100_000), 8388608)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, octal_To_Decimal, 'a')
        self.assertRaises(ValueError, octal_To_Decimal, -10)
        self.assertRaises(ValueError, octal_To_Decimal, 10 ** 10)
