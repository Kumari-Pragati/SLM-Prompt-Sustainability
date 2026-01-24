import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(first_Digit(1), 0)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(20), 2)
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(1000), 1)

    def test_edge(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(9), 9)
        self.assertEqual(first_Digit(99), 9)
        self.assertEqual(first_Digit(999), 9)

    def test_large(self):
        self.assertEqual(first_Digit(10000), 1)
        self.assertEqual(first_Digit(100000), 1)
        self.assertEqual(first_Digit(1000000), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            first_Digit(-1)
        with self.assertRaises(ValueError):
            first_Digit(-10)
