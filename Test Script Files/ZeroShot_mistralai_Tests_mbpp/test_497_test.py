import unittest
from mbpp_497_code import pi, sqrt
from your_module import surfacearea_cone  # replace 'your_module' with the actual module name where the function is defined

class TestSurfaceAreaCone(unittest.TestCase):

    def test_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cone(0, 1), 0, delta=1e-6)

    def test_zero_height(self):
        self.assertAlmostEqual(surfacearea_cone(1, 0), pi, delta=1e-6)

    def test_small_values(self):
        self.assertAlmostEqual(surfacearea_cone(0.1, 0.2), 0.20155, delta=1e-6)

    def test_large_values(self):
        self.assertAlmostEqual(surfacearea_cone(100, 200), 314159.2653589793, delta=1e-6)

    def test_negative_values(self):
        self.assertRaises(ValueError, surfacearea_cone, -1, 2)
        self.assertRaises(ValueError, surfacearea_cone, 2, -1)
