import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_simple_cuboid(self):
        self.assertEqual(volume_cuboid(1, 2, 3), 6)
        self.assertEqual(volume_cuboid(2, 2, 2), 8)
        self.assertEqual(volume_cuboid(3, 3, 3), 27)

    def test_edge_cases(self):
        self.assertEqual(volume_cuboid(0, 2, 3), 0)
        self.assertEqual(volume_cuboid(1, 0, 3), 0)
        self.assertEqual(volume_cuboid(1, 2, 0), 0)
        self.assertEqual(volume_cuboid(1, 1, 0), 0)
        self.assertEqual(volume_cuboid(0, 0, 3), 0)
        self.assertEqual(volume_cuboid(0, 1, 0), 0)
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(volume_cuboid(1, 2, 1), 2)
        self.assertEqual(volume_cuboid(1, 1, 1), 1)

    def test_negative_inputs(self):
        self.assertEqual(volume_cuboid(-1, 2, 3), 0)
        self.assertEqual(volume_cuboid(1, -2, 3), 0)
        self.assertEqual(volume_cuboid(1, 2, -3), 0)

    def test_large_inputs(self):
        self.assertEqual(volume_cuboid(1000, 2000, 3000), 6000000000000)
