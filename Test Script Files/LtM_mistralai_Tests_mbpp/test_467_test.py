import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(25), 31)
        self.assertEqual(decimal_to_Octal(128), 200

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(7), 7)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(255), 377

    def test_complex_inputs(self):
        self.assertEqual(decimal_to_Octal(1001), 1101)
        self.assertEqual(decimal_to_Octal(2047), 5375
