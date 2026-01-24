import unittest
from194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 24)
        self.assertEqual(octal_To_Decimal(37), 55)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(7), 7)
        self.assertEqual(octal_To_Decimal(100), 148)
        self.assertEqual(octal_To_Decimal(255), 327)
        self.assertEqual(octal_To_Decimal(377), 511)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, octal_To_Decimal, 'a')
        self.assertRaises(ValueError, octal_To_Decimal, -1)
        self.assertRaises(ValueError, octal_To_Decimal, 1024)
