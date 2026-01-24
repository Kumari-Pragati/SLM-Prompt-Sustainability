import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_Digit(12), 1)
        self.assertEqual(first_Digit(23), 2)
        self.assertEqual(first_Digit(99), 9)

    def test_edge_conditions(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(999), 9)
        self.assertEqual(first_Digit(1000), 1)

    def test_complex_inputs(self):
        self.assertEqual(first_Digit(1000001), 1)
        self.assertEqual(first_Digit(123456789), 1)
        self.assertEqual(first_Digit(1234567890), 1)
        self.assertEqual(first_Digit(-123456789), 1)
        self.assertEqual(first_Digit(-12345678), 8)
