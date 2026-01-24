import unittest
from mbpp_458_code import rectangle_length, rectangle_breadth

class TestRectangleArea(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(5, 4), 20)
        self.assertEqual(rectangle_area(1, 1), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rectangle_area(0, 0), 0)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(-1, 2), 2)
        self.assertEqual(rectangle_area(2, -3), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_area('a', 3)
        with self.assertRaises(TypeError):
            rectangle_area(2, 'b')
