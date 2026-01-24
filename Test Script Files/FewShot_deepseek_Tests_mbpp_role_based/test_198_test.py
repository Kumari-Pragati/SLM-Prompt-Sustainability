import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(largest_triangle(10, 2), 25.98076211353316)

    def test_boundary_condition(self):
        self.assertEqual(largest_triangle(0, 2), 0)

    def test_edge_condition(self):
        self.assertEqual(largest_triangle(1, 0), -1)

    def test_invalid_input(self):
        self.assertEqual(largest_triangle(-1, 2), -1)
        self.assertEqual(largest_triangle(1, -2), -1)
        self.assertEqual(largest_triangle(-1, -2), -1)
