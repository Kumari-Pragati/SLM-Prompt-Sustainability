import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(2), 1)
        self.assertEqual(closest_num(10), 9)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative_numbers(self):
        self.assertEqual(closest_num(-1), -2)
        self.assertEqual(closest_num(-2), -3)
        self.assertEqual(closest_num(-10), -11)
