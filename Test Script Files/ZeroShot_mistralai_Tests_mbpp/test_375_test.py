import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_round_num_positive(self):
        self.assertEqual(round_num(1, 2), 2)
        self.assertEqual(round_num(3, 2), 4)
        self.assertEqual(round_num(5, 2), 6)
        self.assertEqual(round_num(7, 2), 8)
        self.assertEqual(round_num(9, 2), 10)

    def test_round_num_zero(self):
        self.assertEqual(round_num(0, 2), 0)
        self.assertEqual(round_num(-0, 2), 0)

    def test_round_num_negative(self):
        self.assertEqual(round_num(-1, 2), -2)
        self.assertEqual(round_num(-3, 2), -4)
        self.assertEqual(round_num(-5, 2), -6)
        self.assertEqual(round_num(-7, 2), -8)
        self.assertEqual(round_num(-9, 2), -10)

    def test_round_num_fraction(self):
        self.assertEqual(round_num(3.5, 2), 4)
        self.assertEqual(round_num(7.5, 2), 8)
        self.assertEqual(round_num(11.5, 2), 12)
        self.assertEqual(round_num(15.5, 2), 16)
        self.assertEqual(round_num(19.5, 2), 20)
