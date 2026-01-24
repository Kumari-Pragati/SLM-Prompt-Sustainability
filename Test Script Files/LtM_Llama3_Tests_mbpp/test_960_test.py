import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_two(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_three(self):
        self.assertEqual(get_noOfways(3), 2)

    def test_negative(self):
        self.assertEqual(get_noOfways(-1), 0)

    def test_negative_two(self):
        self.assertEqual(get_noOfways(-2), 0)

    def test_large(self):
        self.assertEqual(get_noOfways(10), 55)

    def test_large_two(self):
        self.assertEqual(get_noOfways(20), 676)
