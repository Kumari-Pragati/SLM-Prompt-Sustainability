import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rectangle_area(3, 4), 12)

    def test_zero_length(self):
        self.assertEqual(rectangle_area(0, 4), 0)

    def test_zero_width(self):
        self.assertEqual(rectangle_area(3, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(rectangle_area(-3, 4), 12)

    def test_float_numbers(self):
        self.assertAlmostEqual(rectangle_area(3.5, 4.5), 15.75)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_area('str', 4)
