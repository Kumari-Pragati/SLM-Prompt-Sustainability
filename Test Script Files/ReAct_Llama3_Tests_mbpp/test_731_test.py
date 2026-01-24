import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 10), 78.53981633974483)

    def test_zero_radius(self):
        with self.assertRaises(ZeroDivisionError):
            lateralsurface_cone(0, 10)

    def test_zero_height(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(5, -10)

    def test_large_radius(self):
        self.assertAlmostEqual(lateralsurface_cone(100, 10), 31415.92653589793)

    def test_large_height(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 100), 7853.981633974483)
