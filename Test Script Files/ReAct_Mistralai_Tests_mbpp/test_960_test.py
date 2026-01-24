import unittest
from960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_small_positive_numbers(self):
        for n in range(2, 6):
            self.assertEqual(get_noOfways(n), n - 1)

    def test_large_positive_numbers(self):
        for n in range(10, 20):
            self.assertEqual(get_noOfways(n), sum(range(2, n + 1)))

    def test_negative_numbers(self):
        for n in range(-10, -1, -1):
            self.assertRaises(ValueError, get_noOfways, n)

    def test_zero_or_negative_input(self):
        self.assertRaises(ValueError, get_noOfways, 0)
        self.assertRaises(ValueError, get_noOfways, -1)
