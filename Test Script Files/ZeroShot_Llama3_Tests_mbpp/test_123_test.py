import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(amicable_numbers_sum(100), 31626)

    def test_non_integer_input(self):
        self.assertEqual(amicable_numbers_sum("100"), "Input is not an integer!")

    def test_limit_less_than_one(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_limit_one(self):
        self.assertEqual(amicable_numbers_sum(1), 1)

    def test_limit_two(self):
        self.assertEqual(amicable_numbers_sum(2), 2)

    def test_limit_three(self):
        self.assertEqual(amicable_numbers_sum(3), 3)

    def test_limit_four(self):
        self.assertEqual(amicable_numbers_sum(4), 4)

    def test_limit_five(self):
        self.assertEqual(amicable_numbers_sum(5), 5)

    def test_limit_six(self):
        self.assertEqual(amicable_numbers_sum(6), 6)

    def test_limit_seven(self):
        self.assertEqual(amicable_numbers_sum(7), 6)

    def test_limit_eight(self):
        self.assertEqual(amicable_numbers_sum(8), 6)

    def test_limit_nine(self):
        self.assertEqual(amicable_numbers_sum(9), 6)

    def test_limit_ten(self):
        self.assertEqual(amicable_numbers_sum(10), 6)
