import unittest
from mbpp_458_code import rectangle_length, rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_zero_length(self):
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_zero_breadth(self):
        self.assertEqual(rectangle_area(4, 0), 0)

    def test_zero_length_and_breadth(self):
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_negative_length(self):
        self.assertEqual(rectangle_area(-4, 5), 20)

    def test_negative_breadth(self):
        self.assertEqual(rectangle_area(4, -5), 20)

    def test_positive_and_negative_length(self):
        self.assertEqual(rectangle_area(4, -5), 20)

    def test_positive_and_negative_breadth(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_non_numeric_length(self):
        with self.assertRaises(TypeError):
            rectangle_area('a', 5)

    def test_non_numeric_breadth(self):
        with self.assertRaises(TypeError):
            rectangle_area(4, 'b')
