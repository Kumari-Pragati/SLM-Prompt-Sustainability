import unittest
from mbpp_458_code import rectangle_length, rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_positive_length_and_breadth(self):
        self.assertEqual(rectangle_area(5, 3), 15)

    def test_zero_length_and_breadth(self):
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_negative_length_and_breadth(self):
        self.assertEqual(rectangle_area(-5, -3), 15)

    def test_length_zero_breadth_positive(self):
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_length_positive_breadth_zero(self):
        self.assertEqual(rectangle_area(5, 0), 0)

    def test_length_and_breadth_as_strings(self):
        with self.assertRaises(TypeError):
            rectangle_area('5', '3')

    def test_length_as_string_breadth_positive(self):
        with self.assertRaises(TypeError):
            rectangle_area('5', 3)

    def test_length_positive_breadth_as_string(self):
        with self.assertRaises(TypeError):
            rectangle_area(5, '3')
