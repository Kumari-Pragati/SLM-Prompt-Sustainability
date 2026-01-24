import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(5), 101)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(16), 10000)
        self.assertEqual(decimal_To_Binary(32), 100000)
        self.assertEqual(decimal_To_Binary(64), 1000000)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('a')
        with self.assertRaises(TypeError):
            decimal_To_Binary(None)
