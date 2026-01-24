import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_sum_nums_within_range(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(7, 4, 10, 20), None)
        self.assertEqual(sum_nums(2, 3, 1, 5), None)

    def test_sum_nums_outside_range(self):
        self.assertEqual(sum_nums(5, 3, 0, 5), None)
        self.assertEqual(sum_nums(7, 4, 21, 20), None)
        self.assertEqual(sum_nums(2, 3, -1, 5), None)
