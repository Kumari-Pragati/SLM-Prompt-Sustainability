import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 10), 78.53981633974483)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 10), 0)
        self.assertAlmostEqual(lateralsurface_cone(5, 0), 0)

    def test_edge_case_zero_radius(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 10), 0)

    def test_edge_case_zero_height(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone('five', 10)
        with self.assertRaises(TypeError):
            lateralsurface_cone(5, 'ten')

    def test_negative_inputs(self):
        self.assertAlmostEqual(lateralsurface_cone(-5, 10), 78.53981633974483)
        self.assertAlmostEqual(lateralsurface_cone(5, -10), 78.53981633974483)

    def test_zero_inputs(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 10), 0)
        self.assertAlmostEqual(lateralsurface_cone(5, 0), 0)
