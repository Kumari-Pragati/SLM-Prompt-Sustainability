import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)
        self.assertEqual(volume_cuboid(1, 1, 1), 1)

    def test_edge_conditions(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)
        self.assertEqual(volume_cuboid(1, 0, 0), 0)
        self.assertEqual(volume_cuboid(0, 1, 0), 0)
        self.assertEqual(volume_cuboid(0, 0, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(volume_cuboid(100, 100, 100), 1000000)
        self.assertEqual(volume_cuboid(1, 1000000, 1000000), 1000000000000)

    def test_complex_cases(self):
        self.assertEqual(volume_cuboid(1000, 2000, 3000), 6000000000)
        self.assertEqual(volume_cuboid(0.5, 1.5, 2.5), 1.875)
