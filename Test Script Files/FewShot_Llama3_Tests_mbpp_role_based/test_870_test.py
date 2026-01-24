import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_single_positive_number(self):
        self.assertEqual(sum_positivenum([1]), 1)

    def test_multiple_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_single_negative_number(self):
        self.assertEqual(sum_positivenum([-1]), 0)

    def test_multiple_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, 2, -3, 4, -5]), 1)

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_list_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            sum_positivenum([1, 2, 'a', 4, 5])
