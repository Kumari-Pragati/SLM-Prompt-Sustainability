import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 56)

    def test_boundary_conditions(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)
        self.assertEqual(lateralsurface_cuboid(1, 1, 1), 8)

    def test_edge_conditions(self):
        self.assertEqual(lateralsurface_cuboid(1000, 1000, 1000), 6000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid("3", 4, 5)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, "4", 5)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, 4, "5")
        with self.assertRaises(ValueError):
            lateralsurface_cuboid(-1, 4, 5)
        with self.assertRaises(ValueError):
            lateralsurface_cuboid(3, -4, 5)
        with self.assertRaises(ValueError):
            lateralsurface_cuboid(3, 4, -5)
