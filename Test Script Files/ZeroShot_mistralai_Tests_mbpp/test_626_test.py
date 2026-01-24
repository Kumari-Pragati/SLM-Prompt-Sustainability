import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_negative_radius(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_zero_radius(self):
        self.assertEqual(triangle_area(0), 0)

    def test_positive_radius(self):
        self.assertAlmostEqual(triangle_area(1), 1.0, delta=0.01)
        self.assertAlmostEqual(triangle_area(2), 12.566370614359172, delta=0.01)
        self.assertAlmostEqual(triangle_area(3), 28.274333882308138, delta=0.01)
