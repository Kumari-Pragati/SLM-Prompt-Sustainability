import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(closest_num(10), 9)
        self.assertEqual(closest_num(20), 19)
        self.assertEqual(closest_num(100), 99)

    def test_negative_numbers(self):
        self.assertEqual(closest_num(-10), -11)
        self.assertEqual(closest_num(-20), -21)
        self.assertEqual(closest_num(-100), -101)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_large_numbers(self):
        self.assertEqual(closest_num(1000000), 999999)
