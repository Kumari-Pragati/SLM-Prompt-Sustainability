import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 3)
        self.assertEqual(last_Two_Digits(4), 4)
        self.assertEqual(last_Two_Digits(5), 5)
        self.assertEqual(last_Two_Digits(6), 6)
        self.assertEqual(last_Two_Digits(7), 7)
        self.assertEqual(last_Two_Digits(8), 8)
        self.assertEqual(last_Two_Digits(9), 9)
        self.assertEqual(last_Two_Digits(10), 0)
        self.assertEqual(last_Two_Digits(11), 1)
        self.assertEqual(last_Two_Digits(12), 2)
        self.assertEqual(last_Two_Digits(13), 3)
        self.assertEqual(last_Two_Digits(14), 4)
        self.assertEqual(last_Two_Digits(15), 5)
        self.assertEqual(last_Two_Digits(16), 6)
        self.assertEqual(last_Two_Digits(17), 7)
        self.assertEqual(last_Two_Digits(18), 8)
        self.assertEqual(last_Two_Digits(19), 9)
        self.assertEqual(last_Two_Digits(20), 0)

    def test_large_numbers(self):
        self.assertEqual(last_Two_Digits(100), 0)
        self.assertEqual(last_Two_Digits(1000), 0)
        self.assertEqual(last_Two_Digits(10000), 0)
        self.assertEqual(last_Two_Digits(100000), 0)
        self.assertEqual(last_Two_Digits(1000000), 0)
        self.assertEqual(last_Two_Digits(10000000), 0)
        self.assertEqual(last_Two_Digits(100000000), 0)
        self.assertEqual(last_Two_Digits(1000000000), 0)

    def test_zero(self):
        self.assertEqual(last_Two_Digits(0), 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, last_Two_Digits, -1)
        self.assertRaises(ValueError, last_Two_Digits, -2)
        self.assertRaises(ValueError, last_Two_Digits, -3)
        self.assertRaises(ValueError, last_Two_Digits, -4)
        self.assertRaises(ValueError, last_Two_Digits, -5)
        self.assertRaises(ValueError, last_Two_Digits, -6)
        self.assertRaises(ValueError, last_Two_Digits, -7)
        self.assertRaises(ValueError, last_Two_Digits, -8)
        self.assertRaises(ValueError, last_Two_Digits, -9)
