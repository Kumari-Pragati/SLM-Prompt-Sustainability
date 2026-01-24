import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_rectangle_perimeter_positive(self):
        # Typical case: positive integer inputs
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(5, 10), 30)

    def test_rectangle_perimeter_zero(self):
        # Edge case: zero length or breadth
        self.assertEqual(rectangle_perimeter(0, 4), 0)
        self.assertEqual(rectangle_perimeter(3, 0), 0)

    def test_rectangle_perimeter_negative(self):
        # Edge case: negative integer inputs
        self.assertEqual(rectangle_perimeter(-3, 4), 14)
        self.assertEqual(rectangle_perimeter(3, -4), 14)

    def test_rectangle_perimeter_float(self):
        # Edge case: float inputs
        self.assertAlmostEqual(rectangle_perimeter(3.5, 4.5), 19.5, delta=0.01)

    def test_rectangle_perimeter_non_number(self):
        # Error case: non-number inputs
        self.assertRaises(TypeError, rectangle_perimeter, 'a', 4)
        self.assertRaises(TypeError, rectangle_perimeter, 3, 'b')
