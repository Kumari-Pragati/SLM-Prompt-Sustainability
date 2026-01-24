import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(find_ways(4), 3)
        self.assertEqual(find_ways(6), 5)

    def test_edge_and_boundary(self):
        self.assertEqual(find_ways(1), 0)
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(3), 1)
        self.assertEqual(find_ways(5), 2)
        self.assertEqual(find_ways(10), 9)

    def test_complex_input(self):
        self.assertEqual(find_ways(15), 38)
        self.assertEqual(find_ways(21), 105)
        self.assertEqual(find_ways(33), 448)
