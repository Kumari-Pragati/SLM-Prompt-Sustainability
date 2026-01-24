import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_typical_cases(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_negative_numbers(self):
        with self.assertRaises(Exception):
            get_noOfways(-1)

    def test_large_numbers(self):
        self.assertGreater(get_noOfways(20), 0)
