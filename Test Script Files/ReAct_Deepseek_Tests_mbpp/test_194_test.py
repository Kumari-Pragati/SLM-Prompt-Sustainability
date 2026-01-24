import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('123'), 83)
        self.assertEqual(octal_To_Decimal('777'), 511)

    def test_edge_cases(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('7777777'), 4095)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            octal_To_Decimal(10)
        with self.assertRaises(ValueError):
            octal_To_Decimal('8888')
