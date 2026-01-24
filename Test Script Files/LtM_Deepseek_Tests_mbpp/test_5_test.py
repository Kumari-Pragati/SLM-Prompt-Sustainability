import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 2)

    def test_edge_conditions(self):
        self.assertEqual(count_ways(-1), 1)
        self.assertEqual(count_ways(3), 4)

    def test_complex_cases(self):
        self.assertEqual(count_ways(5), 10)
        self.assertEqual(count_ways(10), 44)
