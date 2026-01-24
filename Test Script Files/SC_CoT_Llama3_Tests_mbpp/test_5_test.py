import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_ways(3), 2)

    def test_edge_case(self):
        self.assertEqual(count_ways(1), 0)
        self.assertEqual(count_ways(2), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            count_ways(-1)

    def test_edge_case_zero(self):
        self.assertEqual(count_ways(0), 1)

    def test_large_input(self):
        self.assertEqual(count_ways(10), 55)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            count_ways('a')

    def test_invalid_input_non_positive(self):
        with self.assertRaises(ValueError):
            count_ways(0)
