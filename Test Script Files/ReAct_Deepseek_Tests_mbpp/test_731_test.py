import unittest
from mbpp_731_code import lateralsurface_cone

class TestLatersurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(3, 4), 37.6817, places=4)

    def test_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cone(3, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-2, 3)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(2, -3)

    def test_large_numbers(self):
        self.assertAlmostEqual(lateralsurface_cone(1000, 2000), 628318.5307, places=4)
