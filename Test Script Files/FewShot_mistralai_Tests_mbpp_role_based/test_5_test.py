import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_ways(3), 3)
        self.assertEqual(count_ways(4), 5)
        self.assertEqual(count_ways(5), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 1)
        self.assertEqual(count_ways(2), 3)
        self.assertEqual(count_ways(6), 13)
        self.assertEqual(count_ways(7), 20)
