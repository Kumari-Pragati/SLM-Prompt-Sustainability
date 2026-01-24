import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):

    def test_lcm_positive_numbers(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(8, 12), 24)
        self.assertEqual(lcm(15, 20), 60)
        self.assertEqual(lcm(30, 40), 120)
        self.assertEqual(lcm(100, 200), 200)

    def test_lcm_zero(self):
        self.assertRaises(ZeroDivisionError, lcm, 0, 4)
        self.assertRaises(ZeroDivisionError, lcm, 4, 0)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-2, -4), 4)
        self.assertEqual(lcm(-8, -12), 24)
        self.assertEqual(lcm(-15, -20), 60)
        self.assertEqual(lcm(-30, -40), 120)
        self.assertEqual(lcm(-100, -200), 200)

    def test_lcm_one(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)
