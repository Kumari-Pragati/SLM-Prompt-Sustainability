import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(triangle_area(5), 25)

    def test_edge(self):
        self.assertEqual(triangle_area(0), 0)
        self.assertEqual(triangle_area(-1), -1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            triangle_area('a')

    def test_boundary(self):
        self.assertEqual(triangle_area(1), 1)

    def test_large(self):
        self.assertEqual(triangle_area(100), 10000)
