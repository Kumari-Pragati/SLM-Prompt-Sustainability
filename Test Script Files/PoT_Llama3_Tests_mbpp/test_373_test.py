import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(volume_cuboid(3, 4, 5), 60)

    def test_edge_case_zero(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(volume_cuboid(-1, -2, -3), 6)

    def test_edge_case_single_zero(self):
        self.assertEqual(volume_cuboid(3, 0, 5), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(volume_cuboid(3, -2, 5), 30)

    def test_edge_case_all_negative(self):
        self.assertEqual(volume_cuboid(-1, -2, -3), 6)

    def test_edge_case_all_zero(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)
