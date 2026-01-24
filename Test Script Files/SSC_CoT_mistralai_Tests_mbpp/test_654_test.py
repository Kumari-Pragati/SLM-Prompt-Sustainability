import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(5, 5), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rectangle_perimeter(0, 4), 8)
        self.assertEqual(rectangle_perimeter(4, 0), 8)
        self.assertEqual(rectangle_perimeter(1, 1), 4)
        self.assertEqual(rectangle_perimeter(-3, 4), 14)
        self.assertEqual(rectangle_perimeter(3, -4), 14)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 'b')
        with self.assertRaises(TypeError):
            rectangle_perimeter([1, 2], [3, 4])
