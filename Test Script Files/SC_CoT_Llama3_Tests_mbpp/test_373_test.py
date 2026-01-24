import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(volume_cuboid(3, 4, 5), 60)

    def test_edge_cases(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)
        self.assertEqual(volume_cuboid(0, 0, 1), 0)
        self.assertEqual(volume_cuboid(0, 1, 0), 0)
        self.assertEqual(volume_cuboid(0, 1, 1), 0)
        self.assertEqual(volume_cuboid(1, 0, 0), 0)
        self.assertEqual(volume_cuboid(1, 0, 1), 0)
        self.assertEqual(volume_cuboid(1, 1, 0), 0)
        self.assertEqual(volume_cuboid(1, 1, 1), 1)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            volume_cuboid(-1, 2, 3)
        with self.assertRaises(TypeError):
            volume_cuboid(1, -2, 3)
        with self.assertRaises(TypeError):
            volume_cuboid(1, 2, -3)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            volume_cuboid(1.5, 2, 3)
        with self.assertRaises(TypeError):
            volume_cuboid(1, 2.5, 3)
        with self.assertRaises(TypeError):
            volume_cuboid(1, 2, 3.5)
