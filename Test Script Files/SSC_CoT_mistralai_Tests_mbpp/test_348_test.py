import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_ways(4), 3)
        self.assertEqual(find_ways(8), 6)
        self.assertEqual(find_ways(16), 18)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_ways(1), 0)
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(3), 1)
        self.assertEqual(find_ways(5), 2)
        self.assertEqual(find_ways(6), 3)
        self.assertEqual(find_ways(7), 3)
        self.assertEqual(find_ways(9), 6)

    def test_negative_input(self):
        self.assertRaises(ValueError, find_ways, -1)
