import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsufaceCylinder(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 785.3981633974483)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0, 10), 0)
        self.assertAlmostEqual(lateralsuface_cylinder(5, 0), 0)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(-5, 10)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('five', 10)

    def test_zero_radius(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 0), 0)
