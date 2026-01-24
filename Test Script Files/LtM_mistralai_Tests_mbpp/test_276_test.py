import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertAlmostEqual(volume_cylinder(1, 2), 12.566368064500002)
        self.assertAlmostEqual(volume_cylinder(2, 3), 125.663680645)
        self.assertAlmostEqual(volume_cylinder(3, 4), 376.991358025)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(volume_cylinder(0, 1), 0)
        self.assertAlmostEqual(volume_cylinder(1, 0), 0)
        self.assertAlmostEqual(volume_cylinder(1, 1), 3.141592653589793)
        self.assertAlmostEqual(volume_cylinder(1000, 1000), 31415926535897931.000000001)

    def test_negative_inputs(self):
        self.assertAlmostEqual(volume_cylinder(-1, 2), -6.283185307179586)
        self.assertAlmostEqual(volume_cylinder(1, -2), -12.566368064500002)

    def test_complex_inputs(self):
        self.assertAlmostEqual(volume_cylinder(1.5, 2.5), 28.27433388230813)
        self.assertAlmostEqual(volume_cylinder(3.14, 2.718), 2827.433388230813)
