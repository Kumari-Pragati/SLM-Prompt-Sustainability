import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(volume_cylinder(2, 3), 37.699050800802, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_cylinder(0, 3), 0, places=5)
        self.assertAlmostEqual(volume_cylinder(2, 0), 0, places=5)
        self.assertAlmostEqual(volume_cylinder(0, 0), 0, places=5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cylinder('a', 3)
        with self.assertRaises(TypeError):
            volume_cylinder(2, 'b')

    def test_boundary_conditions(self):
        self.assertAlmostEqual(volume_cylinder(1, 1), 3.1415, places=5)
