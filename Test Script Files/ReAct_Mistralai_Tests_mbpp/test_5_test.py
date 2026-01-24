import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_ways(3), 3)
        self.assertEqual(count_ways(4), 5)
        self.assertEqual(count_ways(5), 8)

    def test_edge_cases(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 1)
        self.assertEqual(count_ways(2), 3)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            count_ways(-1)

    def test_zero_input(self):
        with self.assertRaises(TypeError):
            count_ways("abc")
