import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 1)
        self.assertEqual(divisor(3), 2)
        self.assertEqual(divisor(4), 2)
        self.assertEqual(divisor(5), 2)
        self.assertEqual(divisor(6), 3)
        self.assertEqual(divisor(7), 2)
        self.assertEqual(divisor(8), 3)
        self.assertEqual(divisor(9), 2)
        self.assertEqual(divisor(10), 4)

    def test_large_numbers(self):
        self.assertEqual(divisor(100), 25)
        self.assertEqual(divisor(1000), 168)
        self.assertEqual(divisor(10000), 2491)

    def test_prime_numbers(self):
        self.assertEqual(divisor(2), 1)
        self.assertEqual(divisor(3), 2)
        self.assertEqual(divisor(5), 2)
        self.assertEqual(divisor(7), 2)
        self.assertEqual(divisor(11), 2)
        self.assertEqual(divisor(13), 2)
        self.assertEqual(divisor(17), 2)
        self.assertEqual(divisor(19), 2)
        self.assertEqual(divisor(23), 2)
        self.assertEqual(divisor(29), 2)
        self.assertEqual(divisor(31), 2)
        self.assertEqual(divisor(37), 2)
        self.assertEqual(divisor(41), 2)
        self.assertEqual(divisor(43), 2)
        self.assertEqual(divisor(47), 2)
        self.assertEqual(divisor(53), 2)
        self.assertEqual(divisor(59), 2)
        self.assertEqual(divisor(61), 2)
        self.assertEqual(divisor(67), 2)
        self.assertEqual(divisor(71), 2)
        self.assertEqual(divisor(73), 2)
        self.assertEqual(divisor(79), 2)
        self.assertEqual(divisor(83), 2)
        self.assertEqual(divisor(89), 2)
        self.assertEqual(divisor(97), 2)

    def test_zero(self):
        self.assertRaises(ValueError, divisor, 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, divisor, -1)
        self.assertRaises(ValueError, divisor, -2)
        self.assertRaises(ValueError, divisor, -3)
        self.assertRaises(ValueError, divisor, -4)
        self.assertRaises(ValueError, divisor, -5)
        self.assertRaises(ValueError, divisor, -6)
        self.assertRaises(ValueError, divisor, -7)
        self.assertRaises(ValueError, divisor, -8)
        self.assertRaises(ValueError, divisor, -9)
        self.assertRaises(ValueError, divisor, -10)
