import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_ways(0), 1)

    def test_one(self):
        self.assertEqual(count_ways(1), 1)

    def test_small_numbers(self):
        self.assertEqual(count_ways(2), 2)
        self.assertEqual(count_ways(3), 3)
        self.assertEqual(count_ways(4), 5)
        self.assertEqual(count_ways(5), 8)

    def test_large_numbers(self):
        self.assertEqual(count_ways(10), 55)
        self.assertEqual(count_ways(15), 610)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_ways('a')
