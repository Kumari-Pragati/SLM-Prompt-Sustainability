import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_sum_nums_within_range(self):
        self.assertEqual(sum_nums(5, 10, 15, 30), 20)

    def test_sum_nums_outside_range(self):
        self.assertEqual(sum_nums(1, 2, 3, 4), 3)

    def test_sum_nums_with_negative_numbers(self):
        self.assertEqual(sum_nums(-5, 5, -10, 10), 20)

    def test_sum_nums_with_zero(self):
        self.assertEqual(sum_nums(0, 0, 0, 0), 0)
