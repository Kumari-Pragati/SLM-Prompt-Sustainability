import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 1)
        self.assertEqual(count_ways(3), 2)
        self.assertEqual(count_ways(4), 3)

    def test_edge(self):
        self.assertEqual(count_ways(-1), None)
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 1)
        self.assertEqual(count_ways(3), 2)

    def test_large(self):
        self.assertEqual(count_ways(5), 5)
        self.assertEqual(count_ways(10), 55)
        self.assertEqual(count_ways(15), 89)
