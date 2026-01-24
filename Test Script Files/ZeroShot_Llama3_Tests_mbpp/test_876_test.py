import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):

    def test_lcm_positive(self):
        self.assertEqual(lcm(2, 3), 6)

    def test_lcm_negative(self):
        self.assertEqual(lcm(-2, -3), 6)

    def test_lcm_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 3)

    def test_lcm_zero2(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(3, 0)

    def test_lcm_negative_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(-2, 0)

    def test_lcm_negative_zero2(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, -3)

    def test_lcm_positive_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(2, 0)

    def test_lcm_negative_zero3(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(-2, 0)
