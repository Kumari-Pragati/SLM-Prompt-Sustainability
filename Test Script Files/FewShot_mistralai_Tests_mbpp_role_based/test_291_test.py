import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_no_of_ways(5, 2), 5)
        self.assertEqual(count_no_of_ways(10, 3), 45)
        self.assertEqual(count_no_of_ways(20, 4), 1970)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 1)
        self.assertEqual(count_no_of_ways(3, 1), 2)
        self.assertEqual(count_no_of_ways(4, 1), 3)
        self.assertEqual(count_no_of_ways(5, 1), 5)
        self.assertEqual(count_no_of_ways(0, k=2), 0)
        self.assertEqual(count_no_of_ways(1, 0), 0)
        self.assertEqual(count_no_of_ways(1, k=0), 0)
        self.assertEqual(count_no_of_ways(n=-1, k=2), 0)
        self.assertEqual(count_no_of_ways(n=0, k=-1), 0)
        self.assertEqual(count_no_of_ways(n=-1, k=-1), 0)
