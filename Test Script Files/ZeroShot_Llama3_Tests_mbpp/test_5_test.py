import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_count_ways_zero(self):
        self.assertEqual(count_ways(0), 1)

    def test_count_ways_one(self):
        self.assertEqual(count_ways(1), 0)

    def test_count_ways_two(self):
        self.assertEqual(count_ways(2), 2)

    def test_count_ways_three(self):
        self.assertEqual(count_ways(3), 3)

    def test_count_ways_four(self):
        self.assertEqual(count_ways(4), 5)

    def test_count_ways_five(self):
        self.assertEqual(count_ways(5), 8)

    def test_count_ways_six(self):
        self.assertEqual(count_ways(6), 13)

    def test_count_ways_negative(self):
        with self.assertRaises(ValueError):
            count_ways(-1)

    def test_count_ways_non_integer(self):
        with self.assertRaises(TypeError):
            count_ways('a')
