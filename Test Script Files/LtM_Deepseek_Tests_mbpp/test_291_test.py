import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_no_of_ways(1, 2), 2)
        self.assertEqual(count_no_of_ways(2, 3), 9)

    def test_edge_conditions(self):
        self.assertEqual(count_no_of_ways(0, 1), 0)
        self.assertEqual(count_no_of_ways(1, 0), 0)
        self.assertEqual(count_no_of_ways(0, 0), 0)
        self.assertEqual(count_no_of_ways(100, 1), 1)
        self.assertEqual(count_no_of_ways(1, 100), 100)

    def test_complex_cases(self):
        self.assertEqual(count_no_of_ways(10, 2), 1048576)
        self.assertEqual(count_no_of_ways(15, 3), 14348907)
