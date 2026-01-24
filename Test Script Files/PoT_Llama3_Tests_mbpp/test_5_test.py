import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_ways(3), 2)

    def test_edge_case(self):
        self.assertEqual(count_ways(1), 1)
        self.assertEqual(count_ways(2), 2)

    def test_boundary_case(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(4), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_ways('a')
