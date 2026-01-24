import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(first_Digit(12345), 5)
        self.assertEqual(first_Digit(98765), 6)
        self.assertEqual(first_Digit(10000), 0)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(first_Digit(-123), 1)
        self.assertEqual(first_Digit(-987), 7)
        self.assertEqual(first_Digit(-1000), 0)

    def test_large_numbers(self):
        self.assertEqual(first_Digit(123456789), 7)
        self.assertEqual(first_Digit(987654321), 1)

    def test_fractional_numbers(self):
        self.assertEqual(first_Digit(12.345), 5)
        self.assertEqual(first_Digit(98.765), 8)

    def test_empty_string(self):
        self.assertEqual(first_Digit(''), 0)

    def test_non_numeric_inputs(self):
        self.assertRaises(ValueError, first_Digit, 'abc')
        self.assertRaises(ValueError, first_Digit, [1, 2, 3])
        self.assertRaises(ValueError, first_Digit, (1, 2, 3))
        self.assertRaises(ValueError, first_Digit, None)
        self.assertRaises(ValueError, first_Digit, True)
        self.assertRaises(ValueError, first_Digit, False)
