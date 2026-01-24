import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_Nth_Digit(123456789, 10, 1), 8)
        self.assertEqual(find_Nth_Digit(1234567890, 10, 9), 9)
        self.assertEqual(find_Nth_Digit(1234567890123, 100, 100), 1)

    def test_small_input(self):
        self.assertEqual(find_Nth_Digit(1, 10, 1), 1)
        self.assertEqual(find_Nth_Digit(12, 10, 1), 2)
        self.assertEqual(find_Nth_Digit(123, 10, 1), 3)
        self.assertEqual(find_Nth_Digit(1234, 10, 1), 4)
        self.assertEqual(find_Nth_Digit(12345, 10, 1), 5)

    def test_large_input(self):
        self.assertEqual(find_Nth_Digit(1234567890123456789, 10, 17), 9)
        self.assertEqual(find_Nth_Digit(1234567890123456789, 10, 18), 0)

    def test_zero_input(self):
        self.assertEqual(find_Nth_Digit(0, 10, 1), 0)

    def test_negative_input(self):
        self.assertRaises(ValueError, find_Nth_Digit, -123456789, 10, 1)
        self.assertRaises(ValueError, find_Nth_Digit, 123456789, -10, 1)
        self.assertRaises(ValueError, find_Nth_Digit, 123456789, 10, 0)
        self.assertRaises(ValueError, find_Nth_Digit, 123456789, 10, -1)
