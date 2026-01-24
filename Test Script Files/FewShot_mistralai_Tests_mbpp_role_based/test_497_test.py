import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):
    def test_positive_radius_and_height(self):
        self.assertAlmostEqual(surfacearea_cone(2, 3), math.pi * 2 * (2 + math.sqrt(2 * 2 + 3 * 3)))

    def test_zero_radius_and_height(self):
        self.assertEqual(surfacearea_cone(0, 0), 0)

    def test_negative_radius_and_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-1, -2)

    def test_zero_radius_and_positive_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(0, 3)

    def test_positive_radius_and_zero_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(2, 0)
