import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_positive_normal(self):
        self.assertEqual(triangle_area(3), 9)

    def test_zero(self):
        self.assertEqual(triangle_area(0), 0)

    def test_negative(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_small_positive(self):
        self.assertEqual(triangle_area(0.5), 0.25)

    def test_large_positive(self):
        self.assertEqual(triangle_area(100), 10000)
