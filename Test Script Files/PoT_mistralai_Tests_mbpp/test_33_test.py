import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(255), 11111111)
        self.assertEqual(decimal_To_Binary(1024), 10000000)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(decimal_To_Binary(0), '0')
        self.assertEqual(decimal_To_Binary(1), '1')
        self.assertEqual(decimal_To_Binary(2), '10')
        self.assertEqual(decimal_To_Binary(3), '11')
        self.assertEqual(decimal_To_Binary(4), '100')
        self.assertEqual(decimal_To_Binary(5), '101')
        self.assertEqual(decimal_To_Binary(6), '110')
        self.assertEqual(decimal_To_Binary(7), '111')
        self.assertEqual(decimal_To_Binary(8), '1000')
        self.assertEqual(decimal_To_Binary(9), '1001')
        self.assertEqual(decimal_To_Binary(1023), '11111111')
        self.assertEqual(decimal_To_Binary(1023 + 1), '10000000001')
