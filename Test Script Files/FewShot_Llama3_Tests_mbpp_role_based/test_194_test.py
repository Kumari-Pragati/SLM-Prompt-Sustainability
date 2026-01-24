import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_valid_octal_numbers(self):
        self.assertEqual(octal_To_Decimal(12), 10)
        self.assertEqual(octal_To_Decimal(25), 21)
        self.assertEqual(octal_To_Decimal(100), 64)

    def test_edge_cases(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(1), 1)
        self.assertEqual(octal_To_Decimal(8), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal('abc')
        with self.assertRaises(TypeError):
            octal_To_Decimal(None)
