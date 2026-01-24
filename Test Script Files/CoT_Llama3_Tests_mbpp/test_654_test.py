import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(10, 5), 20)
        self.assertEqual(rectangle_perimeter(7, 2), 18)

    def test_edge_cases(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(5, 0), 10)
        self.assertEqual(rectangle_perimeter(0, 5), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 3)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, 'b')
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 'b')

    def test_negative_inputs(self):
        self.assertEqual(rectangle_perimeter(-5, 3), 12)
        self.assertEqual(rectangle_perimeter(5, -3), 12)
