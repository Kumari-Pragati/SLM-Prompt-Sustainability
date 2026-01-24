import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([8, 16]), 32)
        self.assertEqual(get_lcm([10, 20]), 100)

    def test_three_numbers(self):
        self.assertEqual(get_lcm([2, 4, 6]), 12)
        self.assertEqual(get_lcm([8, 16, 24]), 96)
        self.assertEqual(get_lcm([10, 20, 30]), 600)

    def test_zero(self):
        self.assertEqual(get_lcm([0, 0]), 0)
        self.assertEqual(get_lcm([2, 0]), 0)
        self.assertEqual(get_lcm([0, 2]), 0)

    def test_negative_numbers(self):
        self.assertEqual(get_lcm([-2, -4]), 8)
        self.assertEqual(get_lcm([-8, -16]), 32)
        self.assertEqual(get_lcm([-10, -20]), 100)

    def test_one_number(self):
        self.assertEqual(get_lcm([2]), 2)
        self.assertEqual(get_lcm([-2]), 2)
        self.assertEqual(get_lcm([0]), 0)
