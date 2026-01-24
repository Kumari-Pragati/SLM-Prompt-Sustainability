import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):

    def test_lcm_positive_numbers(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-4, -6), 12)

    def test_lcm_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 6)

    def test_lcm_zero_and_non_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 6)

    def test_lcm_non_zero_and_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(6, 0)

    def test_lcm_non_integer(self):
        with self.assertRaises(TypeError):
            lcm(4.5, 6)

    def test_lcm_non_numeric(self):
        with self.assertRaises(TypeError):
            lcm('a', 6)
