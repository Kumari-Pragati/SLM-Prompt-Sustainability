import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_edge_input(self):
        self.assertEqual(volume_cuboid(0, 3, 4), 0)
        self.assertEqual(volume_cuboid(2, 0, 4), 0)
        self.assertEqual(volume_cuboid(2, 3, 0), 0)

    def test_boundary_input(self):
        self.assertEqual(volume_cuboid(1, 1, 1), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, volume_cuboid, -1, 3, 4)
        self.assertRaises(ValueError, volume_cuboid, 2, -1, 4)
        self.assertRaises(ValueError, volume_cuboid, 2, 3, -1)
