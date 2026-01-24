import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(15), 1111)
        self.assertEqual(decimal_To_Binary(32), 100000)

    def test_edge_cases(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(8), 1000)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('10')
        with self.assertRaises(ValueError):
            decimal_To_Binary(-10)
