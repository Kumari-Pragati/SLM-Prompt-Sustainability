import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_ways(4), 2)
        self.assertEqual(find_ways(6), 3)
        self.assertEqual(find_ways(8), 4)

    def test_odd_input(self):
        self.assertRaises(ValueError, find_ways, 1)
        self.assertRaises(ValueError, find_ways, 3)

    def test_zero_input(self):
        self.assertEqual(find_ways(0), 0)
