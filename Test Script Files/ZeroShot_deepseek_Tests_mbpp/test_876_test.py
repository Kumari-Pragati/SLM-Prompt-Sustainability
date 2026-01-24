import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):

    def test_lcm_positive_numbers(self):
        self.assertEqual(lcm(4, 5), 20)
        self.assertEqual(lcm(15, 10), 30)
        self.assertEqual(lcm(21, 14), 42)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-4, -5), 20)
        self.assertEqual(lcm(-15, -10), 30)
        self.assertEqual(lcm(-21, -14), 42)

    def test_lcm_mixed_numbers(self):
        self.assertEqual(lcm(-4, 5), 20)
        self.assertEqual(lcm(15, -10), 30)
        self.assertEqual(lcm(-21, 14), 42)

    def test_lcm_zero(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(15, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_lcm_equal_numbers(self):
        self.assertEqual(lcm(5, 5), 5)
        self.assertEqual(lcm(10, 10), 10)
        self.assertEqual(lcm(0, 0), 0)
