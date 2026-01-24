import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_positive(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_all_negative(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -2)

    def test_large_numbers(self):
        self.assertEqual(sum_negativenum([-1000, 2000, -3000]), -4000)

    def test_float_numbers(self):
        self.assertAlmostEqual(sum_negativenum([1.5, -2.5, 3.5]), -1.0)

    def test_mixed_float_and_int(self):
        self.assertAlmostEqual(sum_negativenum([1, -2.5, 3, -4.5]), -4.0)
