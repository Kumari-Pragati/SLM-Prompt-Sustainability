import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopbottomSurfaceArea(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 78.53982)

    def test_zero_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea(-5)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea('five')
