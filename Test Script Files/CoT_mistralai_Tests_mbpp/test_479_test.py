import unittest
from479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(987), 9)
        self.assertEqual(first_Digit(56), 5)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_integer(self):
        self.assertEqual(first_Digit(-123), 1)
        self.assertEqual(first_Digit(-987), -9)
        self.assertEqual(first_Digit(-56), -5)

    def test_floats(self):
        self.assertEqual(first_Digit(123.45), 1)
        self.assertEqual(first_Digit(-123.45), 1)
        self.assertEqual(first_Digit(0.01), 0)

    def test_edge_cases(self):
        self.assertEqual(first_Digit(9.999), 9)
        self.assertEqual(first_Digit(0.001), 0)
        self.assertEqual(first_Digit(1000000000), 1)
