import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_single_positive(self):
        self.assertEqual(sum_positivenum([1]), 1)

    def test_multiple_positive(self):
        self.assertEqual(sum_positivenum([1, 2, 3]), 6)

    def test_single_negative(self):
        self.assertEqual(sum_positivenum([-1]), 0)

    def test_multiple_negative(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_mixed_positive_negative(self):
        self.assertEqual(sum_positivenum([-1, 2, -3, 4]), 5)

    def test_max_value(self):
        self.assertEqual(sum_positivenum([2147483647]), 2147483647)

    def test_min_value(self):
        self.assertEqual(sum_positivenum([-2147483648]), 0)

    def test_max_value_negative(self):
        self.assertEqual(sum_positivenum([-2147483648, 2147483647]), 2147483647)

    def test_max_value_negative_mixed(self):
        self.assertEqual(sum_positivenum([-2147483648, 2147483647, -1, 2]), 2147483647)
