import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_positive_small(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_positive_large(self):
        self.assertEqual(get_noOfways(10), 36)
        self.assertEqual(get_noOfways(20), 1027)
        self.assertEqual(get_noOfways(30), 35279)

    def test_negative(self):
        self.assertRaises(ValueError, get_noOfways, -1)
