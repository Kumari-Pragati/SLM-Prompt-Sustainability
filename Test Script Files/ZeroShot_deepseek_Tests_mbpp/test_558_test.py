import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(123, 456), 6)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, -456), 6)

    def test_mixed_numbers(self):
        self.assertEqual(digit_distance_nums(-123, 456), 6)

    def test_same_numbers(self):
        self.assertEqual(digit_distance_nums(123, 123), 0)

    def test_zero_and_positive(self):
        self.assertEqual(digit_distance_nums(0, 123), 3)

    def test_zero_and_negative(self):
        self.assertEqual(digit_distance_nums(0, -123), 3)

    def test_zero_and_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
