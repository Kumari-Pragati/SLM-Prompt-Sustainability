import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 1, -2, 2, -3]), -4)

    def test_zero(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_negativenum([-1000000, 1000000, -2000000, 2000000]), -1000000)

    def test_float_numbers(self):
        self.assertAlmostEqual(sum_negativenum([-3.14, 2.71, -4.14]), -5.85)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_negativenum(1.23456)
