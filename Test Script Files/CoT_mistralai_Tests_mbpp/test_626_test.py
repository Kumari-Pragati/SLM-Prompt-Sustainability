import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(triangle_area(3), 9)

    def test_zero(self):
        self.assertEqual(triangle_area(0), 0)

    def test_negative_number(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_large_number(self):
        self.assertEqual(triangle_area(1000), 1000000000)

    def test_small_number(self):
        self.assertEqual(triangle_area(0.001), 0.000000003)
