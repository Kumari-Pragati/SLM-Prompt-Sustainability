import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_sum_within_range(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(-3, -4, -10, -20), 20)
        self.assertEqual(sum_nums(0, 0, 0, 0), 0)

    def test_sum_outside_range(self):
        self.assertNotEqual(sum_nums(5, 3, 10, 5), 20)
        self.assertNotEqual(sum_nums(-3, -4, -10, -5), 20)
        self.assertNotEqual(sum_nums(0, 0, 0, 5), 0)

    def test_negative_arguments(self):
        self.assertEqual(sum_nums(-2, -3, -10, -20), 20)
        self.assertEqual(sum_nums(-2, 3, -10, -20), sum_nums(2, -3, 10, 20))
        self.assertEqual(sum_nums(2, -3, -10, 20), sum_nums(2, 3, 10, 20))

    def test_zero_arguments(self):
        self.assertEqual(sum_nums(0, 0, 0, 0), 0)
