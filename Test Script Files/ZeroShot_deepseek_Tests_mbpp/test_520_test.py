import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):

    def test_lcm_two_numbers(self):
        self.assertEqual(get_lcm([2, 7]), 14)
        self.assertEqual(get_lcm([3, 5]), 15)
        self.assertEqual(get_lcm([10, 15]), 30)

    def test_lcm_multiple_numbers(self):
        self.assertEqual(get_lcm([2, 7, 11]), 154)
        self.assertEqual(get_lcm([3, 5, 7]), 105)
        self.assertEqual(get_lcm([10, 15, 20]), 60)

    def test_lcm_with_zero(self):
        self.assertEqual(get_lcm([0, 5]), 0)
        self.assertEqual(get_lcm([2, 0]), 0)
        self.assertEqual(get_lcm([0, 0]), 0)

    def test_lcm_with_negative_numbers(self):
        self.assertEqual(get_lcm([-2, 7]), -14)
        self.assertEqual(get_lcm([3, -5]), -15)
        self.assertEqual(get_lcm([-10, 15]), -30)
