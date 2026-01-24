import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(triangle_area(5), 25)
        self.assertEqual(triangle_area(10), 100)

    def test_negative_input(self):
        self.assertEqual(triangle_area(-1), -1)
        self.assertEqual(triangle_area(-5), -1)

    def test_zero_input(self):
        self.assertEqual(triangle_area(0), 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            triangle_area('a')
