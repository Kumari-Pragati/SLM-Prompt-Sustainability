import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 1)
        self.assertEqual(count_ways(3), 2)
        self.assertEqual(count_ways(4), 4)
        self.assertEqual(count_ways(5), 7)

    def test_edge_and_boundary(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(6), 13)
        self.assertEqual(count_ways(7), 20)
        self.assertEqual(count_ways(8), 35)
        self.assertEqual(count_ways(9), 56)
