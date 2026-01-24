import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_count_Digit_positive(self):
        self.assertEqual(count_Digit(123), 3)

    def test_count_Digit_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_count_Digit_negative(self):
        self.assertEqual(count_Digit(-123), 3)

    def test_count_Digit_negative_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_count_Digit_non_integer(self):
        with self.assertRaises(TypeError):
            count_Digit('123')

    def test_count_Digit_non_integer_negative(self):
        with self.assertRaises(TypeError):
            count_Digit('-123')
