import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_lcm_of_two_positive_numbers(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_lcm_of_two_negative_numbers(self):
        self.assertEqual(lcm(-4, -6), 12)

    def test_lcm_of_positive_and_negative_numbers(self):
        self.assertEqual(lcm(4, -6), 12)

    def test_lcm_of_zero_and_nonzero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 5)

    def test_lcm_of_nonzero_and_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(5, 0)

    def test_lcm_of_zero_and_zero(self):
        with self.assertRaises(ZeroDivisionError):
            lcm(0, 0)
