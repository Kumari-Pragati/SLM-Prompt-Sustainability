import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(volume_cylinder(1, 2), 6.283)
        self.assertAlmostEqual(volume_cylinder(2, 3), 12.566)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_cylinder(0, 0), 0)
        self.assertAlmostEqual(volume_cylinder(0, 1), 0)
        self.assertAlmostEqual(volume_cylinder(1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cylinder('a', 2)
        with self.assertRaises(TypeError):
            volume_cylinder(1, 'b')
