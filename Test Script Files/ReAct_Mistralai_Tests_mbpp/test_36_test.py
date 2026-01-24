import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_find_first_digit(self):
        self.assertEqual(find_Nth_Digit(1, 10, 1), 1)

    def test_find_small_number_digit(self):
        self.assertEqual(find_Nth_Digit(1, 10, 2), 0)

    def test_find_large_number_digit(self):
        self.assertEqual(find_Nth_Digit(100, 10, 3), 0)

    def test_find_digit_at_end_of_number(self):
        self.assertEqual(find_Nth_Digit(10000, 10, 5), 0)

    def test_find_digit_beyond_number_length(self):
        self.assertEqual(find_Nth_Digit(10000, 10, 6), 1)

    def test_find_digit_with_zero_division(self):
        with self.assertRaises(ZeroDivisionError:
            find_Nth_Digit(0, 10, 1)

    def test_find_digit_with_negative_base(self):
        with self.assertRaises(ValueError):
            find_Nth_Digit(10, -10, 1)
