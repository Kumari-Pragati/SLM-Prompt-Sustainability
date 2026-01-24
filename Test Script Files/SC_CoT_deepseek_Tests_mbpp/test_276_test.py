import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cylinder(5, 10), 785.3975, places=3)

    def test_boundary_case(self):
        self.assertAlmostEqual(volume_cylinder(0, 10), 0)
        self.assertAlmostEqual(volume_cylinder(5, 0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(volume_cylinder(1, 1), 3.1415)
        self.assertAlmostEqual(volume_cylinder(10, 100), 31415.9265, places=3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cylinder("5", 10)
        with self.assertRaises(TypeError):
            volume_cylinder(5, "10")
        with self.assertRaises(ValueError):
            volume_cylinder(-5, 10)
        with self.assertRaises(ValueError):
            volume_cylinder(5, -10)
