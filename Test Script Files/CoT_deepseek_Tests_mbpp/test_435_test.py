import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(456), 6)
        self.assertEqual(last_Digit(789), 9)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-456), 6)
        self.assertEqual(last_Digit(-789), 9)

    def test_single_digit_numbers(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(5), 5)
        self.assertEqual(last_Digit(9), 9)

    def test_large_numbers(self):
        self.assertEqual(last_Digit(1000000000), 0)
        self.assertEqual(last_Digit(999999999), 9)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            last_Digit('123')
        with self.assertRaises(TypeError):
            last_Digit(None)
        with self.assertRaises(TypeError):
            last_Digit([1, 2, 3])
