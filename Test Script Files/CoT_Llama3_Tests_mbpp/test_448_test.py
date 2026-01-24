import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):
    def test_cal_sum_zero(self):
        self.assertEqual(cal_sum(0), 3)

    def test_cal_sum_one(self):
        self.assertEqual(cal_sum(1), 3)

    def test_cal_sum_two(self):
        self.assertEqual(cal_sum(2), 5)

    def test_cal_sum_three(self):
        self.assertEqual(cal_sum(3), 8)

    def test_cal_sum_four(self):
        self.assertEqual(cal_sum(4), 11)

    def test_cal_sum_five(self):
        self.assertEqual(cal_sum(5), 13)

    def test_cal_sum_negative(self):
        with self.assertRaises(TypeError):
            cal_sum(-1)

    def test_cal_sum_non_integer(self):
        with self.assertRaises(TypeError):
            cal_sum(3.5)
