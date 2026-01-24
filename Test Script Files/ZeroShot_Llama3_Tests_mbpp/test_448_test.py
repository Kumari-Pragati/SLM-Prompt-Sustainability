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

    def test_cal_sum_six(self):
        self.assertEqual(cal_sum(6), 16)

    def test_cal_sum_seven(self):
        self.assertEqual(cal_sum(7), 20)

    def test_cal_sum_eight(self):
        self.assertEqual(cal_sum(8), 23)

    def test_cal_sum_nine(self):
        self.assertEqual(cal_sum(9), 25)

    def test_cal_sum_ten(self):
        self.assertEqual(cal_sum(10), 28)
