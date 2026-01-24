import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_ways(3), 4)

    def test_typical_use_case_2(self):
        self.assertEqual(count_ways(5), 13)

    def test_boundary_condition(self):
        self.assertEqual(count_ways(0), 1)

    def test_boundary_condition_2(self):
        self.assertEqual(count_ways(1), 0)

    def test_edge_condition(self):
        self.assertEqual(count_ways(2), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_ways('a')

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            count_ways(None)
