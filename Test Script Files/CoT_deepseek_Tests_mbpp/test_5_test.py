import unittest
from mbpp_5_code import count_ways

class TestCountWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_ways(2), 4)

    def test_typical_case_2(self):
        self.assertEqual(count_ways(3), 10)

    def test_boundary_case(self):
        self.assertEqual(count_ways(0), 1)

    def test_boundary_case_2(self):
        self.assertEqual(count_ways(1), 0)

    def test_edge_case(self):
        self.assertEqual(count_ways(20), 165580141)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_ways('2')

        with self.assertRaises(TypeError):
            count_ways(2.5)

        with self.assertRaises(TypeError):
            count_ways(None)

        with self.assertRaises(ValueError):
            count_ways(-5)
