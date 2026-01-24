import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(10, 20), 1)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-10, -20), 1)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_negative_to_positive(self):
        self.assertEqual(digit_distance_nums(-10, 10), 1)

    def test_positive_to_negative(self):
        self.assertEqual(digit_distance_nums(10, -10), 1)

    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(1000, 2000), 2)

    def test_small_numbers(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)
