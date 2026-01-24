import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_ways(4), 3)
        self.assertEqual(find_ways(6), 5)
        self.assertEqual(find_ways(8), 7)

    def test_edge_case(self):
        self.assertEqual(find_ways(1), 0)
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(3), 1)

    def test_boundary_case(self):
        self.assertEqual(find_ways(0), 0)
        self.assertEqual(find_ways(1000000), 500000)
