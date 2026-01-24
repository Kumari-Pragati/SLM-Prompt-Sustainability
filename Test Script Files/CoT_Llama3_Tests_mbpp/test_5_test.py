import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_ways(0), 1)

    def test_one(self):
        self.assertEqual(count_ways(1), 0)

    def test_two(self):
        self.assertEqual(count_ways(2), 1)

    def test_three(self):
        self.assertEqual(count_ways(3), 2)

    def test_four(self):
        self.assertEqual(count_ways(4), 3)

    def test_five(self):
        self.assertEqual(count_ways(5), 5)

    def test_negative(self):
        with self.assertRaises(ValueError):
            count_ways(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            count_ways('a')
