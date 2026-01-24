import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_digit_distance_nums_positive(self):
        self.assertEqual(digit_distance_nums(12, 15), 3)
        self.assertEqual(digit_distance_nums(123, 456), 5)
        self.assertEqual(digit_distance_nums(1234, 5678), 6)

    def test_digit_distance_nums_negative(self):
        self.assertEqual(digit_distance_nums(-12, -15), 3)
        self.assertEqual(digit_distance_nums(-123, -456), 5)
        self.assertEqual(digit_distance_nums(-1234, -5678), 6)

    def test_digit_distance_nums_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_digit_distance_nums_same_num(self):
        self.assertEqual(digit_distance_nums(123, 123), 0)
