import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(cal_sum(0), 3)

    def test_one(self):
        self.assertEqual(cal_sum(1), 3)

    def test_two(self):
        self.assertEqual(cal_sum(2), 5)

    def test_three(self):
        self.assertEqual(cal_sum(3), 8)

    def test_four(self):
        self.assertEqual(cal_sum(4), 13)

    def test_five(self):
        self.assertEqual(cal_sum(5), 18)

    def test_negative_one(self):
        self.assertEqual(cal_sum(-1), 3)
