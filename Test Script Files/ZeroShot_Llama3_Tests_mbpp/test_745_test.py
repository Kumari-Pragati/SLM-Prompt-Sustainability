import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_divisible_by_digits(self):
        self.assertEqual(divisible_by_digits(1, 10), [1, 2, 3, 5, 7, 9])
        self.assertEqual(divisible_by_digits(10, 20), [10, 12, 14, 15, 16, 18, 20])
        self.assertEqual(divisible_by_digits(20, 30), [20, 24, 25, 26, 27, 28, 30])
        self.assertEqual(divisible_by_digits(1, 1), [1])
        self.assertEqual(divisible_by_digits(1, 2), [1])
        self.assertEqual(divisible_by_digits(1, 3), [1, 2])
        self.assertEqual(divisible_by_digits(1, 4), [1, 2, 3])
        self.assertEqual(divisible_by_digits(1, 5), [1, 2, 3, 4])
        self.assertEqual(divisible_by_digits(1, 6), [1, 2, 3, 4, 5])
        self.assertEqual(divisible_by_digits(1, 7), [1, 2, 3, 4, 5, 6])
        self.assertEqual(divisible_by_digits(1, 8), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(divisible_by_digits(1, 9), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(divisible_by_digits(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(divisible_by_digits(1, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(divisible_by_digits(1, 12), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertEqual(divisible_by_digits(1, 13), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(divisible_by_digits(1, 14), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(divisible_by_digits(1, 15), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(divisible_by_digits(1, 16), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(divisible_by_digits(1, 17), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(divisible_by_digits(1, 18), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
        self.assertEqual(divisible_by_digits(1, 19), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(divisible_by_digits(1, 20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        self.assertEqual(divisible_by_digits(1, 21), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16