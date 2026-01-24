import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_sum_of_two_small_numbers(self):
        self.assertEqual(sum(4, 6), 2)

    def test_sum_of_two_large_numbers(self):
        self.assertEqual(sum(100, 200), 12)

    def test_sum_of_two_equal_numbers(self):
        self.assertEqual(sum(5, 5), 4)

    def test_sum_of_two_numbers_with_no_common_divisor(self):
        self.assertEqual(sum(3, 9), 1)

    def test_sum_of_two_numbers_with_common_divisor(self):
        self.assertEqual(sum(6, 12), 3)

    def test_sum_of_two_negative_numbers(self):
        self.assertEqual(sum(-4, -6), 2)

    def test_sum_of_two_positive_and_negative_numbers(self):
        self.assertEqual(sum(4, -6), 1)

    def test_sum_of_two_zero_numbers(self):
        self.assertEqual(sum(0, 0), 0)

    def test_sum_of_two_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            sum(4.5, 6.7)
