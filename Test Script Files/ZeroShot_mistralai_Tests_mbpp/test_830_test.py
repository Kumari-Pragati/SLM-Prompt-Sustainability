import unittest
from mbpp_830_code import ceil, floor

def round_up(a, digits):
    n = 10**-digits
    return round(ceil(a / n) * n, digits)

class TestRoundUp(unittest.TestCase):

    def test_round_up_with_positive_numbers(self):
        self.assertEqual(round_up(10.12345, 2), 10.12)
        self.assertEqual(round_up(123.45678, 3), 123.457)
        self.assertEqual(round_up(1234.56789, 4), 1234.5679)

    def test_round_up_with_zero(self):
        self.assertEqual(round_up(0.00000, 6), 0.0)

    def test_round_up_with_negative_numbers(self):
        self.assertEqual(round_up(-10.12345, 2), -10.12)
        self.assertEqual(round_up(-123.45678, 3), -123.457)
        self.assertEqual(round_up(-1234.56789, 4), -1234.5679)

    def test_round_up_with_floor(self):
        self.assertEqual(round_up(10.09876, 2), 10.10)
        self.assertEqual(round_up(123.45678, 3), 123.457)
        self.assertEqual(round_up(1234.56789, 4), 1234.5679)

    def test_round_up_with_ceil(self):
        self.assertEqual(round_up(10.00123, 2), 10.01)
        self.assertEqual(round_up(123.00456, 3), 123.005)
        self.assertEqual(round_up(1234.00789, 4), 1234.0079)
