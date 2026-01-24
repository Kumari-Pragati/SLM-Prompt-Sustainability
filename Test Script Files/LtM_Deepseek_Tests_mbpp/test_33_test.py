import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 2)
        self.assertEqual(decimal_To_Binary(2), 4)
        self.assertEqual(decimal_To_Binary(3), 10)
        self.assertEqual(decimal_To_Binary(4), 100)

    def test_edge_conditions(self):
        self.assertEqual(decimal_To_Binary(5), 101)
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(15), 1111)
        self.assertEqual(decimal_To_Binary(31), 11111)

    def test_complex_cases(self):
        self.assertEqual(decimal_To_Binary(60), 111010)
        self.assertEqual(decimal_To_Binary(127), 1111111)
        self.assertEqual(decimal_To_Binary(255), 11111111)
        self.assertEqual(decimal_To_Binary(511), 111111111)
        self.assertEqual(decimal_To_Binary(1023), 1111111111)
