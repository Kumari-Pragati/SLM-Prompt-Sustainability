import unittest
from mbpp_731_code import pi
from mbpp_731_code import lateralsurface_cone

class TestLatersurfaceCone(unittest.TestCase):

    def test_positive_values(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 1), pi * 2)
        self.assertAlmostEqual(lateralsurface_cone(2, 3), pi * 10)
        self.assertAlmostEqual(lateralsurface_cone(5, 12), pi * 65)

    def test_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cone(10, 0), 0)

    def test_negative_values(self):
        self.assertRaises(ValueError, lateralsurface_cone, -1, 1)
        self.assertRaises(ValueError, lateralsurface_cone, 1, -1)
        self.assertRaises(ValueError, lateralsurface_cone, -1, -1)
