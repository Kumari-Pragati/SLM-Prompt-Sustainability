import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_find_ways(self):
        self.assertEqual(find_ways(4), 1)
        self.assertEqual(find_ways(6), 4)
        self.assertEqual(find_ways(8), 14)
        self.assertEqual(find_ways(10), 44)
        self.assertEqual(find_ways(12), 144)
