import unittest
from448_code import cal_sum

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
        self.assertEqual(cal_sum(4), 11)

    def test_negative_one(self):
        self.assertEqual(cal_sum(-1), None)

    def test_large_number(self):
        self.assertEqual(cal_sum(1000), None)

    def test_non_integer(self):
        self.assertEqual(cal_sum(3.14), None)
