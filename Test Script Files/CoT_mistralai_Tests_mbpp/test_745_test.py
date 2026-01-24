import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_empty_range(self):
        self.assertListEqual(divisible_by_digits(0, 0), [])

    def test_single_number(self):
        self.assertListEqual(divisible_by_digits(1, 1), [1])

    def test_simple_range(self):
        self.assertListEqual(divisible_by_digits(1, 10), [2, 4, 6, 8, 10])

    def test_large_range(self):
        self.assertListEqual(divisible_by_digits(1, 100), [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 16, 17, 18, 19, 22, 23, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99])

    def test_negative_numbers(self):
        self.assertListEqual(divisible_by_digits(-10, -1), [])
        self.assertListEqual(divisible_by_digits(-1, 0), [])
        self.assertListEqual(divisible_by_digits(-1, -10), [-1, -2, -3, -4, -5, -6, -7, -8, -9])

    def test_edge_cases(self):
        self.assertListEqual(divisible_by_digits(0, 0), [])
        self.assertListEqual(divisible_by_digits(0, 1), [])
        self.assertListEqual(divisible_by_digits(1, 0), [1])
        self.assertListEqual(divisible_by_digits(10, 10), [10])
        self.assertListEqual(divisible_by_digits(10, 11), [])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, divisible_by_digits, 'a', 'b')
        self.assertRaises(TypeError, divisible_by_digits, 1, 'b')
        self.assertRaises(TypeError, divisible_by_digits, 'a', 1)
        self.assertRaises(ValueError, divisible_by_digits, 1, 0)
