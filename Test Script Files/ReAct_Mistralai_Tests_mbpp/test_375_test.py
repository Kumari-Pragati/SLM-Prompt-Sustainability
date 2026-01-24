import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_round_normal(self):
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(11, 5), 15)
        self.assertEqual(round_num(12, 5), 15)
        self.assertEqual(round_num(13, 5), 15)
        self.assertEqual(round_num(14, 5), 15)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(16, 5), 20)
        self.assertEqual(round_num(17, 5), 20)
        self.assertEqual(round_num(18, 5), 20)
        self.assertEqual(round_num(19, 5), 20)
        self.assertEqual(round_num(20, 5), 20)

    def test_round_zero(self):
        self.assertEqual(round_num(0, 5), 0)
        self.assertEqual(round_num(-1, 5), 0)
        self.assertEqual(round_num(-2, 5), 0)
        self.assertEqual(round_num(-3, 5), 0)
        self.assertEqual(round_num(-4, 5), 0)
        self.assertEqual(round_num(-5, 5), 0)
        self.assertEqual(round_num(-6, 5), 0)
        self.assertEqual(round_num(-7, 5), 0)
        self.assertEqual(round_num(-8, 5), 0)
        self.assertEqual(round_num(-9, 5), 0)
        self.assertEqual(round_num(-10, 5), 0)

    def test_round_negative(self):
        self.assertEqual(round_num(-11, 5), -15)
        self.assertEqual(round_num(-12, 5), -15)
        self.assertEqual(round_num(-13, 5), -15)
        self.assertEqual(round_num(-14, 5), -15)
        self.assertEqual(round_num(-15, 5), -15)
        self.assertEqual(round_num(-16, 5), -20)
        self.assertEqual(round_num(-17, 5), -20)
        self.assertEqual(round_num(-18, 5), -20)
        self.assertEqual(round_num(-19, 5), -20)
        self.assertEqual(round_num(-20, 5), -20)

    def test_round_zero_division(self):
        self.assertEqual(round_num(0, 0), 0)

    def test_round_negative_division(self):
        with self.assertRaises(ValueError):
            round_num(-1, 0)
