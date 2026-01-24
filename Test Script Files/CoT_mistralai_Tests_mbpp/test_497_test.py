import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(surfacearea_cone(1, 2), math.pi * 5)
        self.assertAlmostEqual(surfacearea_cone(3, 4), math.pi * 25)

    def test_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cone(0, 1), math.pi)

    def test_zero_height(self):
        self.assertAlmostEqual(surfacearea_cone(1, 0), math.pi * 2)

    def test_negative_values(self):
        self.assertAlmostEqual(surfacearea_cone(-1, 2), math.pi * (-1 - math.sqrt(1 + 4)))
        self.assertAlmostEqual(surfacearea_cone(3, -4), math.pi * 25 - math.pi * 4)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, surfacearea_cone, 0, 0)
        self.assertRaises(TypeError, surfacearea_cone, 'a', 1)
