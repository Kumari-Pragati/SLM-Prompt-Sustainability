import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 1+2+3+4+5+6+7+8+9)

    def test_single_digit_numbers(self):
        self.assertEqual(sum_of_digits([0, 9]), 0+9)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits([-123, -456]), 1+2+3+4+5+6)

    def test_large_numbers(self):
        self.assertEqual(sum_of_digits([1000000000, 2000000000]), 1+0+0+0+0+0+0+0+0+1+2+0+0+0+0+0+0+0+0+0)

    def test_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_of_digits([123, '456', 789])

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            sum_of_digits([123, [456], 789])
