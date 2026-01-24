import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 16)
        self.assertEqual(octal_To_Decimal(30), 24)

    def test_edge_conditions(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(7777777), 4095)

    def test_boundary_conditions(self):
        self.assertEqual(octal_To_Decimal(10000000), 4096)
        self.assertEqual(octal_To_Decimal(77777777), 4095999)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal('10')
        with self.assertRaises(ValueError):
            octal_To_Decimal(-10)
        with self.assertRaises(TypeError):
            octal_To_Decimal(10.5)
