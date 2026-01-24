import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_positive(self):
        self.assertEqual(triangle_area(5), 25)

    def test_triangle_area_zero(self):
        self.assertEqual(triangle_area(0), 0)

    def test_triangle_area_negative(self):
        self.assertEqual(triangle_area(-5), -1)

    def test_triangle_area_non_numeric(self):
        with self.assertRaises(TypeError):
            triangle_area('a')
