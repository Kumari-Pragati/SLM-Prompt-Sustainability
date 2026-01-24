import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_boundary_case(self):
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(rectangle_area(1, 1), 1)
        self.assertEqual(rectangle_area(2, 2), 4)
        self.assertEqual(rectangle_area(3, 3), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_area("5", 10)
        with self.assertRaises(TypeError):
            rectangle_area(5, "10")
        with self.assertRaises(TypeError):
            rectangle_area("5", "10")
        with self.assertRaises(ValueError):
            rectangle_area(-5, 10)
        with self.assertRaises(ValueError):
            rectangle_area(5, -10)
        with self.assertRaises(ValueError):
            rectangle_area(-5, -10)
