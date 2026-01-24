import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopbottomSurfacearea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 78.53981633974483)

    def test_zero_radius(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_negative_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(-5), 78.53981633974483)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea('five')
