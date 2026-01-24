import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cuboid(2, 3, 4), 24)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(volume_cuboid(0, 0, 0), 0)
        self.assertAlmostEqual(volume_cuboid(1, 1, 1), 1)
        self.assertAlmostEqual(volume_cuboid(100, 100, 100), 1000000)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_cuboid(0.5, 0.5, 0.5), 0.125)
        self.assertAlmostEqual(volume_cuboid(1000, 1000, 1000), 1000000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cuboid("2", 3, 4)
        with self.assertRaises(TypeError):
            volume_cuboid(2, "3", 4)
        with self.assertRaises(TypeError):
            volume_cuboid(2, 3, "4")
        with self.assertRaises(ValueError):
            volume_cuboid(-1, 3, 4)
        with self.assertRaises(ValueError):
            volume_cuboid(2, -3, 4)
        with self.assertRaises(ValueError):
            volume_cuboid(2, 3, -4)
