import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertAlmostEqual(largest_triangle(1, 2), 1.5)
        self.assertAlmostEqual(largest_triangle(2, 3), 3.0)
        self.assertAlmostEqual(largest_triangle(3, 4), 4.5)

    def test_negative_inputs(self):
        self.assertEqual(largest_triangle(-1, 2), -1)
        self.assertEqual(largest_triangle(1, -2), -1)
        self.assertEqual(largest_triangle(-1, -2), -1)

    def test_zero_inputs(self):
        self.assertEqual(largest_triangle(0, 2), -1)
        self.assertEqual(largest_triangle(2, 0), -1)
        self.assertEqual(largest_triangle(0, 0), -1)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            largest_triangle('a', 2)
        with self.assertRaises(TypeError):
            largest_triangle(2, 'b')
