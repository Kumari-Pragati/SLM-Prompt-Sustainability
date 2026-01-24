import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_no_of_ways(2, 1), 1)
        self.assertEqual(count_no_of_ways(3, 1), 2)
        self.assertEqual(count_no_of_ways(4, 2), 6)
        self.assertEqual(count_no_of_ways(5, 3), 10)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_no_of_ways(0, 1), 0)
        self.assertEqual(count_no_of_ways(1, 0), 0)
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(1000000, 1000000), 1)
        self.assertEqual(count_no_of_ways(1, 1000000), 1)
