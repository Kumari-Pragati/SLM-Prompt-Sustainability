import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsufaceCylinder(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(lateralsuface_cylinder(1, 2), 12.5664)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0, 2), 0)
        self.assertAlmostEqual(lateralsuface_cylinder(1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('a', 2)
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(1, 'b')

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 20), 12566.4)
