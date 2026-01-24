import unittest
from520_code import get_lcm

class TestGetLCM(unittest.TestCase):
    def test_single_numbers(self):
        self.assertEqual(get_lcm([2]), 2)
        self.assertEqual(get_lcm([4]), 4)
        self.assertEqual(get_lcm([1]), 1)

    def test_two_numbers(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([8, 12]), 24)
        self.assertEqual(get_lcm([15, 10]), 30)

    def test_multiple_numbers(self):
        self.assertEqual(get_lcm([2, 4, 6]), 24)
        self.assertEqual(get_lcm([1, 2, 3, 4, 5]), 60)
        self.assertEqual(get_lcm([20, 15, 8]), 80)

    def test_negative_numbers(self):
        self.assertEqual(get_lcm([-2, -3]), 6)
        self.assertEqual(get_lcm([-5, -10]), 10)
        self.assertEqual(get_lcm([-1, 0]), 0)

    def test_zero(self):
        self.assertEqual(get_lcm([0]), 0)
        self.assertEqual(get_lcm([0, 1]), 0)
        self.assertEqual(get_lcm([0, 0]), 0)
