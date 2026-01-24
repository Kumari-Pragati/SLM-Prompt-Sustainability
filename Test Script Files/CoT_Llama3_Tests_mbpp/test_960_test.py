import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_get_no_of_ways_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_get_no_of_ways_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_get_no_of_ways_two(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_get_no_of_ways_three(self):
        self.assertEqual(get_noOfways(3), 3)

    def test_get_no_of_ways_four(self):
        self.assertEqual(get_noOfways(4), 5)

    def test_get_no_of_ways_five(self):
        self.assertEqual(get_noOfways(5), 8)

    def test_get_no_of_ways_negative(self):
        with self.assertRaises(TypeError):
            get_noOfways(-1)

    def test_get_no_of_ways_non_integer(self):
        with self.assertRaises(TypeError):
            get_noOfways('a')
