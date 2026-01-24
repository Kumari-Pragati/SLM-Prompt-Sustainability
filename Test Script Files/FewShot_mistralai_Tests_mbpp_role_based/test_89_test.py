import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(closest_num(5), 4)
        self.assertEqual(closest_num(10), 9)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative_numbers(self):
        self.assertEqual(closest_num(-5), -6)
        self.assertEqual(closest_num(-10), -11)
