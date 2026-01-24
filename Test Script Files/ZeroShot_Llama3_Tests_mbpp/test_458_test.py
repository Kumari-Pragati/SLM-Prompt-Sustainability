import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle_area(5, 3), 15)

    def test_rectangle_area_negative(self):
        with self.assertRaises(TypeError):
            rectangle_area(-5, 3)

    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_rectangle_area_non_numeric(self):
        with self.assertRaises(TypeError):
            rectangle_area('five', 3)

    def test_rectangle_area_non_numeric2(self):
        with self.assertRaises(TypeError):
            rectangle_area(5, 'three')
