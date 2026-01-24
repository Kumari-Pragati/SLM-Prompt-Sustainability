import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('777'), 511)
        self.assertEqual(octal_To_Decimal('123'), 83)

    def test_edge_cases(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('77777777777'), 2147483647)

    def test_boundary_cases(self):
        self.assertEqual(octal_To_Decimal('777777777777'), 2147483647)
        self.assertEqual(octal_To_Decimal('1000000000000'), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal(10)
        with self.assertRaises(ValueError):
            octal_To_Decimal('8888888888888')
        with self.assertRaises(ValueError):
            octal_To_Decimal('1234567890123456789012345678901234567890')
