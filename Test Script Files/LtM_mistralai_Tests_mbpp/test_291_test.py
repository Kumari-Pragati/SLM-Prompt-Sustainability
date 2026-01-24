import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_no_of_ways(2, 2), 4)
        self.assertEqual(count_no_of_ways(3, 2), 7)
        self.assertEqual(count_no_of_ways(4, 2), 13)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(0, k=1), 0)
        self.assertEqual(count_no_of_ways(n=1, k=0), 0)
        self.assertEqual(count_no_of_ways(1000000, 1000000), 1)

    def test_complex_scenarios(self):
        self.assertEqual(count_no_of_ways(5, 3), 15)
        self.assertEqual(count_no_of_ways(10, 4), 210)
        self.assertEqual(count_no_of_ways(20, 5), 1974)
