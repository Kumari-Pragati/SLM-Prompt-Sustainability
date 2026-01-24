import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(count_Digit(5), 1)

    def test_double_digit(self):
        self.assertEqual(count_Digit(12), 2)

    def test_triple_digit(self):
        self.assertEqual(count_Digit(123), 3)

    def test_negative_number(self):
        self.assertEqual(count_Digit(-123), 3)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 1)
