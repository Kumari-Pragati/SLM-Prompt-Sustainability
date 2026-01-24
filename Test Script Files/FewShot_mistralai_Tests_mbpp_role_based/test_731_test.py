import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralSurfaceCone(unittest.TestCase):
    def test_positive_r_and_h(self):
        self.assertAlmostEqual(lateralsurface_cone(2, 3), 2 * math.pi * math.sqrt(2 * 2 + 3 * 3))

    def test_zero_r_and_h(self):
        self.assertEqual(lateralsurface_cone(0, 0), 0)

    def test_negative_r_and_h(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-1, -2)

    def test_zero_r_and_positive_h(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(0, 3)

    def test_positive_r_and_zero_h(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(2, 0)
