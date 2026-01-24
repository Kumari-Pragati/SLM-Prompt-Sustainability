import unittest
from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(5), 101)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(65535), 100000000000001
                         )  # Maximum int value
        self.assertEqual(decimal_To_Binary(65536), 100000000000010
                         )  # Overflow test
        self.assertEqual(decimal_To_Binary(-1), 1)
        self.assertEqual(decimal_To_Binary(-2), 10)
        self.assertEqual(decimal_To_Binary(-3), 11)
        self.assertEqual(decimal_To_Binary(-4), 100)
        self.assertEqual(decimal_To_Binary(-5), 101)
