import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(20, 5), 20)

    def test_negative_numbers(self):
        self.assertEqual(round_num(-10, 5), -10)
        self.assertEqual(round_num(-15, 5), -10)
        self.assertEqual(round_num(-20, 5), -15)

    def test_mixed_numbers(self):
        self.assertEqual(round_num(10, -5), 10)
        self.assertEqual(round_num(-10, -5), -10)

    def test_zero(self):
        self.assertEqual(round_num(0, 5), 0)
        self.assertEqual(round_num(0, -5), 0)

    def test_large_numbers(self):
        self.assertEqual(round_num(1000000, 1000), 1000000)
        self.assertEqual(round_num(-1000000, 1000), -1000000)
