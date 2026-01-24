import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(2), 1)
        self.assertEqual(closest_num(3), 2)
        self.assertEqual(closest_num(4), 3)

    def test_negative_numbers(self):
        self.assertEqual(closest_num(-1), -2)
        self.assertEqual(closest_num(-2), -3)
        self.assertEqual(closest_num(-3), -4)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)
