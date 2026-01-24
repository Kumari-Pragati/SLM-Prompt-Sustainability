import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_positive_inputs(self):
        self.assertAlmostEqual(largest_triangle(5, 5), 12.5, places=5)

    def test_negative_inputs(self):
        self.assertEqual(largest_triangle(-5, 5), -1)

    def test_zero_inputs(self):
        self.assertEqual(largest_triangle(0, 5), -1)

    def test_edge_cases(self):
        self.assertAlmostEqual(largest_triangle(0.1, 0.1), 0.0125, places=5)
        self.assertAlmostEqual(largest_triangle(100, 100), 2500.0, places=5)

    def test_large_inputs(self):
        self.assertAlmostEqual(largest_triangle(1000, 1000), 250000.0, places=5)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            largest_triangle('a', 5)

    def test_mixed_type_inputs(self):
        with self.assertRaises(TypeError):
            largest_triangle(5, 'b')
