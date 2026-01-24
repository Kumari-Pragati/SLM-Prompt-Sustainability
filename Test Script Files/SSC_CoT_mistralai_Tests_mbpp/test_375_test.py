import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(20, 5), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(round_num(0, 1), 0)
        self.assertEqual(round_num(1, 1), 1)
        self.assertEqual(round_num(2, 1), 2)
        self.assertEqual(round_num(4, 1), 4)
        self.assertEqual(round_num(5, 1), 5)
        self.assertEqual(round_num(6, 1), 6)
        self.assertEqual(round_num(7, 1), 7)
        self.assertEqual(round_num(8, 1), 8)
        self.assertEqual(round_num(9, 1), 9)
        self.assertEqual(round_num(10, 1), 10)
        self.assertEqual(round_num(11, 1), 10)
        self.assertEqual(round_num(12, 1), 12)
        self.assertEqual(round_num(-1, 1), -1)
        self.assertEqual(round_num(-2, 1), -2)
        self.assertEqual(round_num(-3, 1), -3)
        self.assertEqual(round_num(-4, 1), -4)
        self.assertEqual(round_num(-5, 1), -5)
        self.assertEqual(round_num(-6, 1), -6)
        self.assertEqual(round_num(-7, 1), -7)
        self.assertEqual(round_num(-8, 1), -8)
        self.assertEqual(round_num(-9, 1), -9)
        self.assertEqual(round_num(-10, 1), -10)
        self.assertEqual(round_num(-11, 1), -10)
        self.assertEqual(round_num(-12, 1), -12)
