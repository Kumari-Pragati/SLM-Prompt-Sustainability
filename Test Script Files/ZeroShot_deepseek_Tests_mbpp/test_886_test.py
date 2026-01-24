import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_sum_num_with_positive_numbers(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_sum_num_with_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, -3, -4, -5]), -3.0)

    def test_sum_num_with_mixed_numbers(self):
        self.assertAlmostEqual(sum_num([-1, 2, -3, 4, -5]), 0.0)

    def test_sum_num_with_zeroes(self):
        self.assertAlmostEqual(sum_num([0, 0, 0, 0, 0]), 0.0)

    def test_sum_num_with_single_number(self):
        self.assertAlmostEqual(sum_num([5]), 5.0)

    def test_sum_num_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            sum_num([])
