import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_find_ways_positive(self):
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(4), 3)
        self.assertEqual(find_ways(6), 15)
        self.assertEqual(find_ways(8), 105)
        self.assertEqual(find_ways(10), 945)

    def test_find_ways_even(self):
        self.assertEqual(find_ways(0), 0)
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(4), 3)
        self.assertEqual(find_ways(6), 15)
        self.assertEqual(find_ways(8), 105)

    def test_find_ways_odd(self):
        self.assertEqual(find_ways(1), 0)
        self.assertEqual(find_ways(3), 0)
        self.assertEqual(find_ways(5), 0)
        self.assertEqual(find_ways(7), 0)
        self.assertEqual(find_ways(9), 0)

    def test_find_ways_zero(self):
        self.assertEqual(find_ways(0), 0)

    def test_find_ways_negative(self):
        self.assertEqual(find_ways(-1), None)
        self.assertEqual(find_ways(-2), None)
        self.assertEqual(find_ways(-3), None)
