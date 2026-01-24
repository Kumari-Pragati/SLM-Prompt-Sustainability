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

    def test_multiple_digits(self):
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

    def test_negative(self):
        self.assertEqual(sum_digits(-1), 1)
        self.assertEqual(sum_digits(-10), 1)
        self.assertEqual(sum_digits(-100), 1)

    def test_large_number(self):
        self.assertEqual(sum_digits(123456789), 45)

    def test_large_negative_number(self):
        self.assertEqual(sum_digits(-123456789), 45)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_digits('a')
