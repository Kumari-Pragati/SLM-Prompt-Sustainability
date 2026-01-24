import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_rectangle_area_positive(self):
        """Test rectangle area with positive values"""
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_rectangle_area_zero(self):
        """Test rectangle area with zero length or breadth"""
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)

    def test_rectangle_area_negative(self):
        """Test rectangle area with negative values"""
        self.assertEqual(rectangle_area(-3, 4), 12)
        self.assertRaises(ValueError, rectangle_area, -3, -4)
