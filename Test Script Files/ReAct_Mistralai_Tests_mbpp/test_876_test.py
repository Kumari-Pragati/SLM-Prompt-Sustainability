import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):

    def test_lcm_positive_numbers(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(8, 12), 24)
        self.assertEqual(lcm(10, 15), 30)

    def test_lcm_zero(self):
        self.assertEqual(lcm(0, 4), 0)
        self.assertEqual(lcm(4, 0), 0)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-2, -4), 4)
        self.assertEqual(lcm(-8, -12), 24)
        self.assertEqual(lcm(-10, -15), 30)

    def test_lcm_one(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)

    def test_lcm_large_numbers(self):
        self.assertEqual(lcm(1000000, 2000000), 2000000)

    def test_lcm_small_numbers(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)

    def test_lcm_same_number(self):
        self.assertEqual(lcm(4, 4), 4)
        self.assertEqual(lcm(10, 10), 10)
