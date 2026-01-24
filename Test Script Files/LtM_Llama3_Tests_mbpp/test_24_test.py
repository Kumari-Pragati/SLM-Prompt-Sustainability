import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('10'), 2)
        self.assertEqual(binary_to_decimal('11'), 3)
        self.assertEqual(binary_to_decimal('100'), 4)
        self.assertEqual(binary_to_decimal('101'), 5)

    def test_edge_cases(self):
        self.assertEqual(binary_to_decimal('0'), 0)
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('111'), 7)
        self.assertEqual(binary_to_decimal('1000'), 8)
        self.assertEqual(binary_to_decimal('1111'), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('abc')
        with self.assertRaises(TypeError):
            binary_to_decimal('123')
        with self.assertRaises(TypeError):
            binary_to_decimal('')

    def test_max_value(self):
        self.assertEqual(binary_to_decimal('11111111'), 255)

    def test_max_value_with_leading_zeros(self):
        self.assertEqual(binary_to_decimal('0000111111'), 255)

    def test_max_value_with_leading_zeros_and_spaces(self):
        self.assertEqual(binary_to_decimal('0000 1111111'), 255)
