import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_find_ways_typical(self):
        self.assertEqual(find_ways(4), 1)
        self.assertEqual(find_ways(6), 2)
        self.assertEqual(find_ways(8), 5)

    def test_find_ways_edge(self):
        self.assertEqual(find_ways(2), 1)
        self.assertEqual(find_ways(3), 1)

    def test_find_ways_invalid(self):
        with self.assertRaises(TypeError):
            find_ways('a')

    def test_find_ways_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_ways(0)
