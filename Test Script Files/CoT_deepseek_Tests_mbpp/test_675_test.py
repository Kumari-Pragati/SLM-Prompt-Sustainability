import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 10, 15, 25), 20)

    def test_sum_within_range(self):
        self.assertEqual(sum_nums(10, 15, 20, 30), 20)

    def test_sum_outside_range(self):
        self.assertEqual(sum_nums(10, 25, 20, 30), 35)

    def test_negative_numbers(self):
        self.assertEqual(sum_nums(-5, -10, -20, -10), 20)

    def test_zero_sum(self):
        self.assertEqual(sum_nums(0, 0, -10, 10), 20)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_nums("5", 10, 15, 25)
