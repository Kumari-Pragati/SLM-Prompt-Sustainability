import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)
        self.assertEqual(volume_cuboid(5, 6, 7), 210)
        self.assertEqual(volume_cuboid(1, 2, 3), 6)

    def test_edge_cases(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)
        self.assertEqual(volume_cuboid(1, 0, 0), 0)
        self.assertEqual(volume_cuboid(0, 1, 0), 0)
        self.assertEqual(volume_cuboid(0, 0, 1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cuboid('a', 2, 3)
        with self.assertRaises(TypeError):
            volume_cuboid(2, 'b', 3)
        with self.assertRaises(TypeError):
            volume_cuboid(2, 3, 'c')
