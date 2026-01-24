import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(123, 456), 9)
        self.assertEqual(digit_distance_nums(987, 654), 7)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, -456), 9)
        self.assertEqual(digit_distance_nums(-987, -654), 7)

    def test_same_numbers(self):
        self.assertEqual(digit_distance_nums(123, 123), 0)

    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(123456789, 987654321), 20)

    def test_small_numbers(self):
        self.assertEqual(digit_distance_nums(0, 1), 1)
        self.assertEqual(digit_distance_nums(1, 0), 1)
