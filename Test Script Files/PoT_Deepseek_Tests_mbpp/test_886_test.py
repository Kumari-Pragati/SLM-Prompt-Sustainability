import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_single_number(self):
        self.assertAlmostEqual(sum_num([5]), 5.0)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            sum_num([])

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, -3, -4, -5]), -3.0)

    def test_zero(self):
        self.assertAlmostEqual(sum_num([0, 0, 0]), 0.0)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(sum_num([1.5, 2.5, 3.5]), 2.5)
