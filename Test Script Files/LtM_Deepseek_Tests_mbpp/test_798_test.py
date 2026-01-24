import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):

    def test_sum_simple_numbers(self):
        self.assertEqual(_sum([1, 2, 3, 4]), 10)

    def test_sum_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3, -4]), -10)

    def test_sum_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_sum_single_number(self):
        self.assertEqual(_sum([5]), 5)

    def test_sum_large_numbers(self):
        self.assertEqual(_sum([1000000, 2000000, 3000000]), 6000000)

    def test_sum_mixed_numbers(self):
        self.assertEqual(_sum([1, -1, 2, -2, 3, -3]), 0)
