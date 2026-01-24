import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):

    def test_two_numbers(self):
        self.assertEqual(get_lcm([2, 7]), 14)
        self.assertEqual(get_lcm([15, 10]), 30)
        self.assertEqual(get_lcm([3, 5]), 15)

    def test_multiple_numbers(self):
        self.assertEqual(get_lcm([2, 7, 11]), 154)
        self.assertEqual(get_lcm([15, 10, 20]), 60)
        self.assertEqual(get_lcm([3, 5, 6]), 30)

    def test_same_numbers(self):
        self.assertEqual(get_lcm([2, 2]), 2)
        self.assertEqual(get_lcm([15, 15]), 15)
        self.assertEqual(get_lcm([3, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(get_lcm([-2, 7]), 14)
        self.assertEqual(get_lcm([15, -10]), 30)
        self.assertEqual(get_lcm([-3, 5]), 15)

    def test_zero(self):
        self.assertEqual(get_lcm([0, 7]), 0)
        self.assertEqual(get_lcm([15, 0]), 0)
        self.assertEqual(get_lcm([0, 0]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_lcm("2", 7)
        with self.assertRaises(TypeError):
            get_lcm([2, "7"])
        with self.assertRaises(TypeError):
            get_lcm([2, 7, "11"])
        with self.assertRaises(TypeError):
            get_lcm("15", "10")
