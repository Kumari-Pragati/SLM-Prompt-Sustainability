import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_empty_range(self):
        self.assertListEqual(divisible_by_digits(0, 0), [])

    def test_single_number(self):
        self.assertListEqual(divisible_by_digits(1, 1), [1])

    def test_positive_range(self):
        self.assertListEqual(divisible_by_digits(1, 10), [2, 3, 4, 6, 7, 8, 9])

    def test_negative_range(self):
        self.assertListEqual(divisible_by_digits(-10, -1), [-2, -1])

    def test_zero_as_start_number(self):
        self.assertListEqual(divisible_by_digits(0, 5), [1, 3, 5])

    def test_zero_as_end_number(self):
        self.assertListEqual(divisible_by_digits(1, 0), [1])

    def test_zero_in_range(self):
        self.assertListEqual(divisible_by_digits(1, 5), [2, 3, 4, 6])

    def test_leading_zeros(self):
        self.assertListEqual(divisible_by_digits(100, 105), [102, 103, 104, 105])

    def test_leading_non_zero_digits(self):
        self.assertListEqual(divisible_by_digits(11, 110), [11, 22, 33, 44, 55, 66, 77, 88, 99])

    def test_leading_non_zero_digits_with_zero(self):
        self.assertListEqual(divisible_by_digits(1011, 10110), [1011])

    def test_leading_zero_digits_with_non_zero(self):
        self.assertListEqual(divisible_by_digits(1001, 10010), [1001])

    def test_leading_zero_digits_with_non_zero_and_zero(self):
        self.assertListEqual(divisible_by_digits(10001, 100010), [10001])

    def test_leading_zero_digits_with_non_zero_and_zero_in_range(self):
        self.assertListEqual(divisible_by_digits(10001, 100010), [10001])
        self.assertListEqual(divisible_by_digits(10002, 100010), [])

    def test_negative_numbers_in_range(self):
        self.assertListEqual(divisible_by_digits(-10, -5), [-11, -9, -7, -6])

    def test_negative_numbers_in_range_with_zero(self):
        self.assertListEqual(divisible_by_digits(-10, -1), [-11, -10])
        self.assertListEqual(divisible_by_digits(-1, -10), [])

    def test_large_numbers(self):
        self.assertListEqual(divisible_by_digits(100000, 100010), [100001, 100002, 100003, 100005, 100006, 100007, 100008, 100009])

    def test_large_numbers_with_leading_zeros(self):
        self.assertListEqual(divisible_by_digits(1000000, 10