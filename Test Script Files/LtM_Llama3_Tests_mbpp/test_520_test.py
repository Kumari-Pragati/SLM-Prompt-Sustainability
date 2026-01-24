import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):
    def test_simple_lcm(self):
        self.assertEqual(get_lcm([2, 3]), 6)
        self.assertEqual(get_lcm([4, 5]), 20)
        self.assertEqual(get_lcm([10, 15]), 30)

    def test_lcm_with_zero(self):
        with self.assertRaises(IndexError):
            get_lcm([0, 1])

    def test_lcm_with_negative(self):
        self.assertEqual(get_lcm([-2, 3]), 6)
        self.assertEqual(get_lcm([2, -3]), 6)

    def test_lcm_with_duplicates(self):
        self.assertEqual(get_lcm([2, 2]), 2)
        self.assertEqual(get_lcm([4, 4]), 4)

    def test_lcm_with_multiple_numbers(self):
        self.assertEqual(get_lcm([2, 3, 4]), 12)
        self.assertEqual(get_lcm([5, 6, 7]), 210)
