import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_rectangle_area_negative(self):
        self.assertRaises(ValueError, rectangle_area, -3, 4)
        self.assertRaises(ValueError, rectangle_area, 3, -4)
        self.assertRaises(ValueError, rectangle_area, 0, -5)
        self.assertRaises(ValueError, rectangle_area, -5, 0)
