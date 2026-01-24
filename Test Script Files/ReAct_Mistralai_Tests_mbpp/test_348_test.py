import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_find_ways_positive(self):
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(4), 3)
        self.assertEqual(find_ways(10), 21)
        self.assertEqual(find_ways(100), 499999998)

    def test_find_ways_zero(self):
        self.assertEqual(find_ways(0), 0)

    def test_find_ways_negative(self):
        self.assertRaises(ValueError, find_ways, -1)

    def test_find_ways_non_integer(self):
        self.assertRaises(TypeError, find_ways, 2.5)

    def test_find_ways_non_power_of_two(self):
        self.assertRaises(ValueError, find_ways, 3)
        self.assertRaises(ValueError, find_ways, 5)
