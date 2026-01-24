import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 1)
        self.assertEqual(count_ways(3), 2)
        self.assertEqual(count_ways(4), 4)
        self.assertEqual(count_ways(5), 7)
        self.assertEqual(count_ways(6), 13)
        self.assertEqual(count_ways(7), 24)
        self.assertEqual(count_ways(8), 44)
        self.assertEqual(count_ways(9), 81)
        self.assertEqual(count_ways(10), 149)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(100), 3542248481792619150)
        self.assertRaises(ValueError, count_ways, -1)
        self.assertRaises(ValueError, count_ways, float('inf'))
