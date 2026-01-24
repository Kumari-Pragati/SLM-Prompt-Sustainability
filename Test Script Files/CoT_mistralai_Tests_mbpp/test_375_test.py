import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_round_num_positive(self):
        self.assertEqual(round_num(10, 3), 10)
        self.assertEqual(round_num(13, 3), 12)
        self.assertEqual(round_num(15, 3), 15)
        self.assertEqual(round_num(18, 3), 18)

    def test_round_num_zero(self):
        self.assertEqual(round_num(0, 3), 0)
        self.assertEqual(round_num(-0, 3), 0)

    def test_round_num_negative(self):
        self.assertEqual(round_num(-10, 3), -10)
        self.assertEqual(round_num(-13, 3), -12)
        self.assertEqual(round_num(-15, 3), -15)
        self.assertEqual(round_num(-18, 3), -18)

    def test_round_num_divisibility(self):
        self.assertEqual(round_num(6, 2), 6)
        self.assertEqual(round_num(12, 2), 12)
        self.assertEqual(round_num(24, 2), 24)
        self.assertEqual(round_num(48, 2), 48)

    def test_round_num_small_divisor(self):
        self.assertEqual(round_num(4, 2), 4)
        self.assertEqual(round_num(9, 2), 8)
        self.assertEqual(round_num(16, 2), 16)
        self.assertEqual(round_num(25, 2), 24)

    def test_round_num_zero_divisor(self):
        self.assertEqual(round_num(0, 0), 0)
        self.assertEqual(round_num(-0, 0), 0)

    def test_round_num_invalid_inputs(self):
        self.assertRaises(TypeError, round_num, 'string', 3)
        self.assertRaises(TypeError, round_num, 10, 'string')
        self.assertRaises(TypeError, round_num, -1, 0)
        self.assertRaises(TypeError, round_num, 1, 0)
