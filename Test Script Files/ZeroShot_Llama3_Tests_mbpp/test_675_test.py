import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_sum_nums_in_range(self):
        self.assertEqual(sum_nums(10, 20, 15, 30), 20)

    def test_sum_nums_out_of_range(self):
        self.assertEqual(sum_nums(10, 20, 5, 15), 30)

    def test_sum_nums_negative_numbers(self):
        self.assertEqual(sum_nums(-10, 20, -15, 30), 10)

    def test_sum_nums_zero(self):
        self.assertEqual(sum_nums(0, 0, 0, 10), 0)

    def test_sum_nums_non_integer(self):
        self.assertEqual(sum_nums(10.5, 20.5, 15, 30), 31)
