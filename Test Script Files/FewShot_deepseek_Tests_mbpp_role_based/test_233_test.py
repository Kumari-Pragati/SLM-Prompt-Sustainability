import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsurfaceCylinder(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 314.15 * 10)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0, 10), 0)
        self.assertAlmostEqual(lateralsuface_cylinder(5, 0), 0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(lateralsuface_cylinder(1, 1000), 31415.9265 * 1000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder("5", 10)
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(5, "10")
        with self.assertRaises(TypeError):
            lateralsuface_cylinder("5", "10")
