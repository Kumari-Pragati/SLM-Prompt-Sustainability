import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(5, 6, 7), 84)
        self.assertEqual(lateralsurface_cuboid(10, 20, 30), 1200)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)
        self.assertEqual(lateralsurface_cuboid(1, 1, 1), 4)
        self.assertEqual(lateralsurface_cuboid(100, 100, 100), 2400)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid('a', 2, 3)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(1, 'b', 3)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(1, 2, 'c')
