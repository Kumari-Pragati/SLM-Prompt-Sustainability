import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_edge_and_boundary_cases(self):
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '1')
        self.assertEqual(decimal_to_binary(4), '100')
        self.assertEqual(decimal_to_binary(5), '101')
        self.assertEqual(decimal_to_binary(6), '110')
        self.assertEqual(decimal_to_binary(7), '111')
        self.assertEqual(decimal_to_binary(8), '1000')
        self.assertEqual(decimal_to_binary(9), '1001')
        self.assertEqual(decimal_to_binary(1023), '10101111')
        self.assertEqual(decimal_to_binary(1024), '10000000')
        self.assertEqual(decimal_to_binary(1025), '10000001')

    def test_negative_numbers(self):
        self.assertEqual(decimal_to_binary(-1), '1' + '0' * 31)
        self.assertEqual(decimal_to_binary(-2), '10' + '0' * 30)
        self.assertEqual(decimal_to_binary(-3), '11' + '0' * 29)
        self.assertEqual(decimal_to_binary(-4), '100' + '0' * 28)
        self.assertEqual(decimal_to_binary(-5), '101' + '0' * 27)
        self.assertEqual(decimal_to_binary(-6), '110' + '0' * 26)
        self.assertEqual(decimal_to_binary(-7), '111' + '0' * 25)
        self.assertEqual(decimal_to_binary(-8), '1000' + '0' * 24)
        self.assertEqual(decimal_to_binary(-9), '1001' + '0' * 23)
        self.assertEqual(decimal_to_binary(-10), '1010' + '0' * 22)
        self.assertEqual(decimal_to_binary(-1023), '10101111' + '0' * 17)
        self.assertEqual(decimal_to_binary(-1024), '10000000' + '1')
        self.assertEqual(decimal_to_binary(-1025), '10000001')
