import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_simple_rounding(self):
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(20, 5), 20)

    def test_rounding_down(self):
        self.assertEqual(round_num(9, 5), 5)
        self.assertEqual(round_num(14, 5), 10)
        self.assertEqual(round_num(19, 5), 15)

    def test_rounding_up(self):
        self.assertEqual(round_num(11, 5), 15)
        self.assertEqual(round_num(16, 5), 20)
        self.assertEqual(round_num(21, 5), 25)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, round_num, 0, 0)

    def test_negative_numbers(self):
        self.assertEqual(round_num(-10, 5), -10)
        self.assertEqual(round_num(-15, 5), -15)
        self.assertEqual(round_num(-20, 5), -20)

    def test_rounding_edge_cases(self):
        self.assertEqual(round_num(-9, 5), -5)
        self.assertEqual(round_num(-14, 5), -10)
        self.assertEqual(round_num(-19, 5), -15)
        self.assertEqual(round_num(-11, 5), -15)
        self.assertEqual(round_num(-16, 5), -20)
        self.assertEqual(round_num(-19, 5), -20)
        self.assertEqual(round_num(-21, 5), -25)
