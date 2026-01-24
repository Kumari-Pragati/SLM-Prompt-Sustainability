import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_single_digit(self):
        self.assertEqual(sum_digits(1), 1)
        self.assertEqual(sum_digits(2), 2)
        self.assertEqual(sum_digits(3), 3)
        self.assertEqual(sum_digits(4), 4)
        self.assertEqual(sum_digits(5), 5)
        self.assertEqual(sum_digits(6), 6)
        self.assertEqual(sum_digits(7), 7)
        self.assertEqual(sum_digits(8), 8)
        self.assertEqual(sum_digits(9), 9)

    def test_two_digits(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(11), 2)
        self.assertEqual(sum_digits(12), 3)
        self.assertEqual(sum_digits(13), 4)
        self.assertEqual(sum_digits(14), 5)
        self.assertEqual(sum_digits(15), 6)
        self.assertEqual(sum_digits(16), 7)
        self.assertEqual(sum_digits(17), 8)
        self.assertEqual(sum_digits(18), 9)
        self.assertEqual(sum_digits(19), 10)
        self.assertEqual(sum_digits(20), 2)

    def test_three_digits(self):
        self.assertEqual(sum_digits(100), 1)
        self.assertEqual(sum_digits(101), 2)
        self.assertEqual(sum_digits(102), 3)
        self.assertEqual(sum_digits(103), 4)
        self.assertEqual(sum_digits(104), 5)
        self.assertEqual(sum_digits(105), 6)
        self.assertEqual(sum_digits(106), 7)
        self.assertEqual(sum_digits(107), 8)
        self.assertEqual(sum_digits(108), 9)
        self.assertEqual(sum_digits(109), 10)
        self.assertEqual(sum_digits(110), 2)

    def test_large_number(self):
        self.assertEqual(sum_digits(123456789), 45)

    def test_negative_number(self):
        self.assertEqual(sum_digits(-123), 6)

    def test_negative_zero(self):
        self.assertEqual(sum_digits(-0), 0)
