import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    def test_edge_case(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(5, 0), 10)

    def test_boundary_case(self):
        self.assertEqual(rectangle_perimeter(1, 1), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter("5", 10)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "10")
        with self.assertRaises(TypeError):
            rectangle_perimeter("5", "10")
