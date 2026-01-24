import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(is_triangleexists(60, 60, 60))

    def test_valid_triangle2(self):
        self.assertTrue(is_triangleexists(90, 30, 60))

    def test_invalid_triangle(self):
        self.assertFalse(is_triangleexists(0, 0, 0))

    def test_invalid_triangle2(self):
        self.assertFalse(is_triangleexists(180, 0, 0))

    def test_invalid_triangle3(self):
        self.assertFalse(is_triangleexists(90, 90, 90))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            is_triangleexists('a', 'b', 'c')
