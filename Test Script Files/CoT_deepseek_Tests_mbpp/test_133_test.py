import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4, -5]), -3)

    def test_large_numbers(self):
        self.assertEqual(sum_negativenum(list(range(-1000, 0, 1))), -500500)

    def test_float_numbers(self):
        self.assertEqual(sum_negativenum([-1.5, 2.3, -3.7, 4.1]), -3.3)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            sum_negativenum([1, -2, '3', -4, 5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_negativenum('1, -2, 3, -4, 5')
