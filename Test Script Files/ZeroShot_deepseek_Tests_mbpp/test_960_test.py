import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_get_noOfways_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_get_noOfways_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_get_noOfways_two(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_get_noOfways_three(self):
        self.assertEqual(get_noOfways(3), 3)

    def test_get_noOfways_negative(self):
        with self.assertRaises(RecursionError):
            get_noOfways(-1)

    def test_get_noOfways_large(self):
        self.assertEqual(get_noOfways(20), 10946)
