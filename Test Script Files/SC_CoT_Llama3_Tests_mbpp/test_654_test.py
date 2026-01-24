import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)

    def test_edge_cases(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(10, 0), 20)
        self.assertEqual(rectangle_perimeter(0, 10), 20)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(-5, 3)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, -3)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 3)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, 'b')

    def test_zero_inputs(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
