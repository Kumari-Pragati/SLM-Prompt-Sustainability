import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 2)
        self.assertEqual(count_ways(3), 4)
        self.assertEqual(count_ways(4), 8)

    def test_edge_cases(self):
        self.assertEqual(count_ways(-1), 1)
        self.assertEqual(count_ways(-2), 0)
        self.assertEqual(count_ways(-3), 2)
        self.assertEqual(count_ways(-4), 4)

    def test_boundary_cases(self):
        self.assertEqual(count_ways(5), 16)
        self.assertEqual(count_ways(10), 1024)

    def test_corner_cases(self):
        self.assertEqual(count_ways(15), 32768)
        self.assertEqual(count_ways(20), 1048576)
