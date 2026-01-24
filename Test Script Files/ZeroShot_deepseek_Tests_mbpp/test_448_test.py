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
        self.assertEqual(cal_sum(3), 9)

    def test_four(self):
        self.assertEqual(cal_sum(4), 15)

    def test_five(self):
        self.assertEqual(cal_sum(5), 25)

    def test_negative(self):
        self.assertEqual(cal_sum(-1), 3)

    def test_large(self):
        self.assertEqual(cal_sum(10), 195)
