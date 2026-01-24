import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_positive_numbers(self):
        """Test that the function correctly calculates the last two digits for positive numbers"""
        test_cases = [(1, 1), (2, 2), (3, 3), (4, 6), (5, 5), (9, 9), (10, 0), (11, 1), (99, 9)]
        for number, expected in test_cases:
            with self.subTest(f"Testing number {number}"):
                self.assertEqual(last_Two_Digits(number), expected)

    def test_zero(self):
        """Test that the function correctly handles the case of zero"""
        self.assertEqual(last_Two_Digits(0), 0)

    def test_negative_numbers(self):
        """Test that the function correctly handles negative numbers"""
        test_cases = [(-1, -1), (-2, -2), (-3, -3), (-4, 46), (-5, 5), (-9, -9), (-10, 0), (-11, 1)]
        for number, expected in test_cases:
            with self.subTest(f"Testing number {number}"):
                self.assertEqual(last_Two_Digits(number), expected)

    def test_large_numbers(self):
        """Test that the function correctly handles large numbers"""
        test_cases = [(1000, 0), (10000, 0), (100000, 0), (1000000, 0), (10000000, 0)]
        for number, expected in test_cases:
            with self.subTest(f"Testing number {number}"):
                self.assertEqual(last_Two_Digits(number), expected)
