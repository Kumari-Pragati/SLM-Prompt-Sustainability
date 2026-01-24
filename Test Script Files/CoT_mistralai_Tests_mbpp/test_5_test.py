import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 1)
        self.assertEqual(count_ways(3), 2)
        self.assertEqual(count_ways(4), 3)
        self.assertEqual(count_ways(5), 5)
        self.assertEqual(count_ways(6), 8)
        self.assertEqual(count_ways(7), 13)
        self.assertEqual(count_ways(8), 20)
        self.assertEqual(count_ways(9), 30)
        self.assertEqual(count_ways(10), 45)

    def test_edge_input(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(100), 67960)

    def test_boundary_input(self):
        self.assertEqual(count_ways(-1), None)
        self.assertEqual(count_ways(100000), None)
