import unittest
from mbpp_99_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(1024), '10000000')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(decimal_to_binary(-1), '10' + '1'*63)
        self.assertEqual(decimal_to_binary(2**32), '1' + '0'*31)
        self.assertEqual(decimal_to_binary(2**64-1), '1' + '0'*63)
        self.assertEqual(decimal_to_binary(0b1000000000000000000000000000000000000000000000000000000000000000), '1' + '0'*64)

    def test_special_cases(self):
        self.assertEqual(decimal_to_binary(0b1000), '1110')
        self.assertEqual(decimal_to_binary(0b11111111111111111111111111111111), '1' + '1'*63)
