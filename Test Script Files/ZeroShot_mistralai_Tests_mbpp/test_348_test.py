import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_find_ways_positive(self):
        test_cases = [(4, 2, 3), (9, 4, 6), (16, 8, 10)]
        for M, expected in test_cases:
            with self.subTest(f"M={M}"):
                self.assertEqual(find_ways(M), expected)

    def test_find_ways_zero(self):
        self.assertEqual(find_ways(0), 0)
        self.assertEqual(find_ways(1), 0)
        self.assertEqual(find_ways(2), 1)

    def test_find_ways_negative(self):
        self.assertRaises(ValueError, find_ways, -1)
        self.assertRaises(ValueError, find_ways, -2)
        self.assertRaises(ValueError, find_ways, -3)
