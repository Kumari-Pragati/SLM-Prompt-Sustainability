import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(amicable_numbers_sum(10), 22)
        self.assertEqual(amicable_numbers_sum(100), 17296)
        self.assertEqual(amicable_numbers_sum(1000), 838240)

    def test_zero(self):
        self.assertRaises(ValueError, amicable_numbers_sum, 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, amicable_numbers_sum, -1)

    def test_non_integer(self):
        self.assertRaises(TypeError, amicable_numbers_sum, 3.14)
