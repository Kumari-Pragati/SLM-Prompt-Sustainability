import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(first_Digit(12), 1)
        self.assertEqual(first_Digit(98), 9)
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(1000), 1)
        self.assertEqual(first_Digit(10000), 1)

    def test_edge_cases(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(2), 2)
        self.assertEqual(first_Digit(3), 3)
        self.assertEqual(first_Digit(4), 4)
        self.assertEqual(first_Digit(5), 5)
        self.assertEqual(first_Digit(6), 6)
        self.assertEqual(first_Digit(7), 7)
        self.assertEqual(first_Digit(8), 8)
        self.assertEqual(first_Digit(9), 9)

    def test_corner_cases(self):
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(11), 1)
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(1234), 1)
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(123456), 1)
        self.assertEqual(first_Digit(1234567), 1)
        self.assertEqual(first_Digit(12345678), 1)
        self.assertEqual(first_Digit(123456789), 1)
        self.assertEqual(first_Digit(1234567890), 1)
        self.assertEqual(first_Digit(12345678901), 1)
