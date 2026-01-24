import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_edge_case_zero(self):
        self.assertEqual(volume_cuboid(0, 3, 4), 0)
        self.assertEqual(volume_cuboid(2, 0, 4), 0)
        self.assertEqual(volume_cuboid(2, 3, 0), 0)

    def test_edge_case_one(self):
        self.assertEqual(volume_cuboid(1, 3, 4), 12)
        self.assertEqual(volume_cuboid(2, 1, 4), 8)
        self.assertEqual(volume_cuboid(2, 3, 1), 6)

    def test_edge_case_negative(self):
        self.assertEqual(volume_cuboid(-1, 3, 4), -12)
        self.assertEqual(volume_cuboid(2, -3, 4), -24)
        self.assertEqual(volume_cuboid(2, 3, -4), -24)
