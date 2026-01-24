import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_normal_input(self):
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

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(100), 3542248481792619150)
        self.assertEqual(count_ways(-1), None)
        self.assertEqual(count_ways(200), None)
