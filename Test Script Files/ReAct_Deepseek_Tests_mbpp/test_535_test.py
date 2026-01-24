import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 3.1415 * 5 * 5)

    def test_zero_radius(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            topbottom_surfacearea(-5)

    def test_large_radius(self):
        self.assertAlmostEqual(topbottom_surfacearea(1000), 3.1415 * 1000 * 1000)
