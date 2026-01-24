import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(1), 3.1415)
        self.assertAlmostEqual(topbottom_surfacearea(2), 12.566)
        self.assertAlmostEqual(topbottom_surfacearea(3), 28.2745)

    def test_zero_radius(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            topbottom_surfacearea(-1)
