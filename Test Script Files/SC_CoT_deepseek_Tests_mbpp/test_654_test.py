import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    def test_boundary_conditions(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(1, 1), 4)

    def test_edge_cases(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(10, 0), 20)

    def test_special_cases(self):
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 13.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter("5", 10)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "10")
        with self.assertRaises(TypeError):
            rectangle_perimeter("5", "10")
        with self.assertRaises(ValueError):
            rectangle_perimeter(-5, 10)
        with self.assertRaises(ValueError):
            rectangle_perimeter(5, -10)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-5, -10)
