import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_cylinder(2, 5), 62.8375, places=3)

    def test_boundary_conditions(self):
        self.assertEqual(volume_cylinder(0, 10), 0)
        self.assertEqual(volume_cylinder(1, 0), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_cylinder(1, 1000), 3141.5, places=3)
        self.assertAlmostEqual(volume_cylinder(1000, 1), 3141592.65, places=3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cylinder("2", 5)
        with self.assertRaises(TypeError):
            volume_cylinder(2, "5")
        with self.assertRaises(TypeError):
            volume_cylinder("2", "5")
        with self.assertRaises(ValueError):
            volume_cylinder(-2, 5)
        with self.assertRaises(ValueError):
            volume_cylinder(2, -5)
