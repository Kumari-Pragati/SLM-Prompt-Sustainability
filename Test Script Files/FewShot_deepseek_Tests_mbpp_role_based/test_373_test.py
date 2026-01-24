import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(volume_cuboid(3, 4, 5), 60)

    def test_boundary_conditions(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)
        self.assertEqual(volume_cuboid(1, 1, 1), 1)
        self.assertEqual(volume_cuboid(100, 100, 100), 1000000)

    def test_edge_conditions(self):
        self.assertEqual(volume_cuboid(1000, 1000, 1000), 1000000000)
        self.assertEqual(volume_cuboid(10000, 10000, 10000), 10000000000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cuboid("3", 4, 5)
        with self.assertRaises(TypeError):
            volume_cuboid(3, "4", 5)
        with self.assertRaises(TypeError):
            volume_cuboid(3, 4, "5")
        with self.assertRaises(TypeError):
            volume_cuboid("3", "4", "5")
