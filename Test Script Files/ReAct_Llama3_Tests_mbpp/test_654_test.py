import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)

    def test_zero_length(self):
        self.assertEqual(rectangle_perimeter(0, 3), 6)

    def test_zero_width(self):
        self.assertEqual(rectangle_perimeter(5, 0), 10)

    def test_zero_length_and_width(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_negative_length(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(-5, 3)

    def test_negative_width(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, -3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('five', 3)

    def test_non_numeric_input2(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, 'three')
