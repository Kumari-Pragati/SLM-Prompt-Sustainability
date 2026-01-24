import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_base_case_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_base_case_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_large_positive_numbers(self):
        self.assertEqual(get_noOfways(10), 36)
        self.assertEqual(get_noOfways(20), 1027)
        self.assertEqual(get_noOfways(30), 30647)

    def test_negative_numbers(self):
        self.assertEqual(get_noOfways(-1), 0)
        self.assertEqual(get_noOfways(-2), 0)
        self.assertEqual(get_noOfways(-3), 0)
