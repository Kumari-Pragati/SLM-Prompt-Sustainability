import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_to_decimal_typical(self):
        self.assertEqual(binary_to_decimal('101'), 5)

    def test_binary_to_decimal_edge_case(self):
        self.assertEqual(binary_to_decimal('1'), 1)

    def test_binary_to_decimal_edge_case2(self):
        self.assertEqual(binary_to_decimal('0'), 0)

    def test_binary_to_decimal_edge_case3(self):
        self.assertEqual(binary_to_decimal('111'), 7)

    def test_binary_to_decimal_edge_case4(self):
        self.assertEqual(binary_to_decimal('1000'), 8)

    def test_binary_to_decimal_edge_case5(self):
        self.assertEqual(binary_to_decimal('1111'), 15)

    def test_binary_to_decimal_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('abc')

    def test_binary_to_decimal_empty_input(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('')
