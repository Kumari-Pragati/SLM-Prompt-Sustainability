import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('12'), 10)
        self.assertEqual(octal_To_Decimal('123'), 83)

    def test_edge_cases(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('1'), 1)
        self.assertEqual(octal_To_Decimal('7'), 7)

    def test_boundary_cases(self):
        self.assertEqual(octal_To_Decimal('100'), 64)
        self.assertEqual(octal_To_Decimal('1234'), 830)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal('abc')
        with self.assertRaises(TypeError):
            octal_To_Decimal(None)
        with self.assertRaises(TypeError):
            octal_To_Decimal(123)
