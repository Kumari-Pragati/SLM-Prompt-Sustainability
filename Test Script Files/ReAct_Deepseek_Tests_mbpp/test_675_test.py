import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 10, 15, 25), 20)

    def test_boundary_case(self):
        self.assertEqual(sum_nums(10, 10, 20, 30), 20)

    def test_edge_case(self):
        self.assertEqual(sum_nums(20, 1, 21, 30), 20)

    def test_sum_greater_than_range(self):
        self.assertEqual(sum_nums(25, 10, 15, 25), 35)

    def test_negative_numbers(self):
        self.assertEqual(sum_nums(-5, -10, -15, -5), -15)

    def test_zero_sum(self):
        self.assertEqual(sum_nums(0, 0, -10, 10), 0)
