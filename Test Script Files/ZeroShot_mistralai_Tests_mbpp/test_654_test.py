import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(1, 1), 4)

    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 5), 0)
        self.assertEqual(rectangle_perimeter(5, 0), 0)

    def test_rectangle_perimeter_negative(self):
        self.assertEqual(rectangle_perimeter(-3, 4), 14)
        self.assertEqual(rectangle_perimeter(3, -4), 14)
