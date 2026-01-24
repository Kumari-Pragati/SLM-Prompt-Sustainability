import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLatersurfaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 314.15 * 10, places=2)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0, 10), 0)
        self.assertAlmostEqual(lateralsuface_cylinder(5, 0), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsuface_cylinder(1, 1000), 314.15 * 1000, places=2)
        self.assertAlmostEqual(lateralsuface_cylinder(1000, 1), 314.15 * 1000, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder("5", 10)
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(5, "10")
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(-5, 10)
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(5, -10)
