import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_Digit(12), 1)
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(987), 9)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(9), 9)
        self.assertEqual(first_Digit(1000), 1)
        self.assertEqual(first_Digit(9999), 9)

    def test_complex_inputs(self):
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(98765), 9)
        self.assertEqual(first_Digit(123456), 1)
        self.assertEqual(first_Digit(987654), 9)
