import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 1+2+3+4+5+6+7+8+9)

    def test_single_digit_numbers(self):
        self.assertEqual(sum_of_digits([1, 2, 3]), 1+2+3)

    def test_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-123, -456, -789]), 1+2+3+4+5+6+7+8+9)

    def test_mixed_positive_negative(self):
        self.assertEqual(sum_of_digits([123, -456, 789]), 1+2+3+4+5+6+7+8+9)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_of_digits([123, '456', 789])

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)
