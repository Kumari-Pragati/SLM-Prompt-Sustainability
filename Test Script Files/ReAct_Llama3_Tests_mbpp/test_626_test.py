import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertEqual(triangle_area(5), 25)

    def test_zero_radius(self):
        self.assertEqual(triangle_area(0), 0)

    def test_negative_radius(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            triangle_area('a')

    def test_radius_as_zero_like_object(self):
        self.assertEqual(triangle_area(0.0), 0.0)

    def test_radius_as_negative_like_object(self):
        self.assertEqual(triangle_area(-0.5), 0.25)
