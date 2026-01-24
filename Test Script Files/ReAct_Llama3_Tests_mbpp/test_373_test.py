import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_edge_case_zero(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(volume_cuboid(-1, -2, -3), 6)

    def test_edge_case_single_zero(self):
        self.assertEqual(volume_cuboid(0, 3, 4), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(volume_cuboid(-1, 3, 4), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(volume_cuboid(-1, -2, -3), 6)
