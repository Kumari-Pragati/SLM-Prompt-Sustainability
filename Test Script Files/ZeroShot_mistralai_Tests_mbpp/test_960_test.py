import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_get_no_of_ways_for_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_get_no_of_ways_for_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_get_no_of_ways_for_small_numbers(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)

    def test_get_no_of_ways_for_large_numbers(self):
        self.assertEqual(get_noOfways(10), 34)
        self.assertEqual(get_noOfways(20), 102)
        self.assertEqual(get_noOfways(30), 274)
