import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)

    def test_edge_cases(self):
        self.assertEqual(decimal_To_Binary(5), 101)
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(15), 1111)
        self.assertEqual(decimal_To_Binary(16), 10000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('a')
        with self.assertRaises(TypeError):
            decimal_To_Binary(None)
