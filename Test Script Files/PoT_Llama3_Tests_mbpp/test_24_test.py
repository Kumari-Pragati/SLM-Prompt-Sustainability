import unittest
from mbpp_24_code import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(binary_to_decimal('101'), 5)
        self.assertEqual(binary_to_decimal('110'), 6)
        self.assertEqual(binary_to_decimal('111'), 7)

    def test_edge_cases(self):
        self.assertEqual(binary_to_decimal('0'), 0)
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('10'), 2)

    def test_boundary_cases(self):
        self.assertEqual(binary_to_decimal('100'), 4)
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('1111'), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            binary_to_decimal('abc')
        with self.assertRaises(TypeError):
            binary_to_decimal(None)
        with self.assertRaises(TypeError):
            binary_to_decimal(123)
