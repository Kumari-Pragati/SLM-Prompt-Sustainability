import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_sum_within_range(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(10, 5, 15, 20), 20)

    def test_sum_outside_range(self):
        self.assertNotEqual(sum_nums(5, 3, 10, 15), 20)
        self.assertNotEqual(sum_nums(10, 5, 5, 10), 20)

    def test_negative_numbers(self):
        self.assertNotEqual(sum_nums(-5, -3, 0, 10), 20)
        self.assertNotEqual(sum_nums(-10, -5, 0, 10), 20)

    def test_zero_numbers(self):
        self.assertEqual(sum_nums(0, 0, 0, 0), 0)
        self.assertNotEqual(sum_nums(0, 0, 1, 1), 20)
