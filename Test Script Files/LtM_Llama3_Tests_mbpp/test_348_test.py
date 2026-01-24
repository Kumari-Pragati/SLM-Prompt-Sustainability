import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(4), 2)
        self.assertEqual(find_ways(6), 3)
        self.assertEqual(find_ways(8), 5)

    def test_edge_cases(self):
        self.assertEqual(find_ways(0), 0)
        self.assertEqual(find_ways(1), 1)
        self.assertEqual(find_ways(3), 1)
        self.assertEqual(find_ways(10), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_ways('a')
        with self.assertRaises(TypeError):
            find_ways(-1)
