import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)

    def test_rectangle_perimeter_negative(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(-5, 3)

    def test_rectangle_perimeter_non_numeric(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('five', 3)

    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_rectangle_perimeter_one(self):
        self.assertEqual(rectangle_perimeter(1, 1), 4)

    def test_rectangle_perimeter_large(self):
        self.assertEqual(rectangle_perimeter(100, 50), 300)
