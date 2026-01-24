import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):
    def test_positive_radius_and_height(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 10), 78.53981633974483)

    def test_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cone(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone(5, -10)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone('five', 10)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone(5, 'ten')
