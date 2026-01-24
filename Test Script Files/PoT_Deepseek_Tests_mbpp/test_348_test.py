import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_ways(4), 1)
        self.assertEqual(find_ways(6), 4)
        self.assertEqual(find_ways(8), 14)

    def test_edge_cases(self):
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(find_ways(1), 1)
        self.assertEqual(find_ways(3), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_ways('a')
        with self.assertRaises(ValueError):
            find_ways(-1)
