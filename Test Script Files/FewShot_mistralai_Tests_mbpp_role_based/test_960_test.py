import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_large_positive_numbers(self):
        self.assertEqual(get_noOfways(10), 34)
        self.assertEqual(get_noOfways(20), 103)
        self.assertEqual(get_noOfways(30), 274)

    def test_negative_numbers(self):
        self.assertEqual(get_noOfways(-1), 0)
        self.assertEqual(get_noOfways(-2), 1)
        self.assertEqual(get_noOfways(-3), 2)
