import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_empty_list(self):
        """Test sum_of_digits with an empty list"""
        self.assertEqual(sum_of_digits([]), 0)

    def test_single_digit(self):
        """Test sum_of_digits with a single digit number"""
        self.assertEqual(sum_of_digits([5]), 5)

    def test_single_non_digit(self):
        """Test sum_of_digits with a single non-digit number"""
        self.assertEqual(sum_of_digits(["abc"]), 0)

    def test_multiple_digits(self):
        """Test sum_of_digits with multiple digit numbers"""
        self.assertEqual(sum_of_digits([123, 456, 789]), 21 + 6 + 9)

    def test_negative_numbers(self):
        """Test sum_of_digits with negative numbers"""
        self.assertEqual(sum_of_digits([-123, -456, -789]), 3 + 6 + 9)

    def test_mixed_types(self):
        """Test sum_of_digits with a list containing mixed types"""
        self.assertEqual(sum_of_digits([123, "abc", 456, -789]), 123 + 6 + 456 - 789)

    def test_zero(self):
        """Test sum_of_digits with zero"""
        self.assertEqual(sum_of_digits([0]), 0)

    def test_large_numbers(self):
        """Test sum_of_digits with large numbers"""
        self.assertEqual(sum_of_digits([123456789]), 6 + 7 + 8 + 9)
