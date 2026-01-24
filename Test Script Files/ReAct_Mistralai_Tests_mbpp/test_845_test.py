import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(find_Digits(0), 0)

    def test_negative_number(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_small_positive_number(self):
        self.assertEqual(find_Digits(2), 1)

    def test_large_positive_number(self):
        self.assertEqual(find_Digits(1000000), 7)

    def test_large_positive_number_with_many_digits(self):
        self.assertEqual(find_Digits(1234567890), 10)

    def test_large_positive_number_with_leading_zeros(self):
        self.assertEqual(find_Digits(01234567890), 10)

    def test_large_positive_number_with_trailing_zeros(self):
        self.assertEqual(find_Digits(12345678900), 10)

    def test_large_positive_number_with_many_leading_and_trailing_zeros(self):
        self.assertEqual(find_Digits(0012345678900), 10)
