import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 261.7993877991494)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 0), 0)
        self.assertAlmostEqual(lateralsurface_cone(1, 0), 3.141592653589793)
        self.assertAlmostEqual(lateralsurface_cone(0, 1), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 1), 4.442882938158366)
        self.assertAlmostEqual(lateralsurface_cone(10, 20), 1316.953512711637)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone("5", 12)
        with self.assertRaises(TypeError):
            lateralsurface_cone(5, "12")
        with self.assertRaises(ValueError):
            lateralsurface_cone(-5, 12)
        with self.assertRaises(ValueError):
            lateralsurface_cone(5, -12)
