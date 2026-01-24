import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_count_ways(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 2)
        self.assertEqual(count_ways(3), 3)
        self.assertEqual(count_ways(4), 5)
        self.assertEqual(count_ways(5), 8)
        self.assertEqual(count_ways(6), 13)
        self.assertEqual(count_ways(7), 21)
        self.assertEqual(count_ways(8), 34)
        self.assertEqual(count_ways(9), 55)
        self.assertEqual(count_ways(10), 89)
