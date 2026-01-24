import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([10, 15]), 30)
        self.assertEqual(get_lcm([20, 30]), 60)

    def test_zero(self):
        self.assertRaises(ValueError, get_lcm, [0, 4])
        self.assertRaises(ValueError, get_lcm, [4, 0])

    def test_negative_numbers(self):
        self.assertEqual(get_lcm([-2, -4]), 4)
        self.assertEqual(get_lcm([-10, -15]), 30)
        self.assertEqual(get_lcm([-20, -30]), 60)

    def test_one_argument(self):
        self.assertEqual(get_lcm([1]), 1)

    def test_single_pair(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([10, 10]), 10)

    def test_large_numbers(self):
        self.assertEqual(get_lcm([999999999, 999999999]), 1999999998)
