import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):

    def test_zero_radius(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            topbottom_surfacearea(-1)

    def test_positive_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(1), 3.141592653589793)

    def test_large_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(1000), 31415926.53589793)
