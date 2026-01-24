import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_count_ways_with_zero(self):
        self.assertEqual(count_ways(0), 1)

    def test_count_ways_with_one(self):
        self.assertEqual(count_ways(1), 1)

    def test_count_ways_with_two(self):
        self.assertEqual(count_ways(2), 3)

    def test_count_ways_with_three(self):
        self.assertEqual(count_ways(3), 5)

    def test_count_ways_with_four(self):
        self.assertEqual(count_ways(4), 13)

    def test_count_ways_with_large_number(self):
        self.assertEqual(count_ways(100), 3542248481792619150)
