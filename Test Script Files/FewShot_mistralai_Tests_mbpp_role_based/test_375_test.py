import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_round_to_nearest(self):
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(9, 5), 5)
        self.assertEqual(round_num(11, 5), 15)

    def test_round_down(self):
        self.assertEqual(round_num(10, 4), 10)
        self.assertEqual(round_num(9, 4), 9)
        self.assertEqual(round_num(11, 4), 12)

    def test_round_up(self):
        self.assertEqual(round_num(10, 6), 12)
        self.assertEqual(round_num(9, 6), 6)
        self.assertEqual(round_num(11, 6), 16)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            round_num(0, 0)
