import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_single_digit(self):
        self.assertEqual(sum_of_digits([5]), 5)

    def test_single_non_digit(self):
        self.assertEqual(sum_of_digits(["a"]), 0)

    def test_multiple_digits(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 21)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-123, -456, -789]), 12)

    def test_mixed_types(self):
        self.assertEqual(sum_of_digits([123, "456", 789]), 1327)

    def test_floats(self):
        self.assertEqual(sum_of_digits([123.456, 789.012]), 1326)
