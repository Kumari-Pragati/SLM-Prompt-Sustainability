import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(cal_sum(0), 3)

    def test_one(self):
        self.assertEqual(cal_sum(1), 3)

    def test_two(self):
        self.assertEqual(cal_sum(2), 5)

    def test_typical_cases(self):
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 13)
        self.assertEqual(cal_sum(5), 21)

    def test_large_number(self):
        self.assertEqual(cal_sum(10), 196)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            cal_sum(-1)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            cal_sum(1.5)
