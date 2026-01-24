import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCones(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(surfacearea_cone(5, 10), 78.53981633974483)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cone(0, 10), 0)
        self.assertAlmostEqual(surfacearea_cone(5, 0), 0)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cone(-5, 10)

        with self.assertRaises(TypeError):
            surfacearea_cone(5, -10)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cone('five', 10)

        with self.assertRaises(TypeError):
            surfacearea_cone(5, 'ten')

    def test_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cone(0, 10), 0)

    def test_zero_height(self):
        self.assertAlmostEqual(surfacearea_cone(5, 0), 0)
