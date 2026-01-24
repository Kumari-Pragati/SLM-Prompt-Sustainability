import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cuboid(3, 4, 5), 56.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lateralsurface_cuboid(0, 0, 0), 0.0)
        self.assertAlmostEqual(lateralsurface_cuboid(1, 1, 1), 12.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsurface_cuboid(0, 5, 10), 0.0)
        self.assertAlmostEqual(lateralsurface_cuboid(5, 0, 10), 0.0)
        self.assertAlmostEqual(lateralsurface_cuboid(10, 5, 0), 0.0)

    def test_special_cases(self):
        self.assertAlmostEqual(lateralsurface_cuboid(2.5, 3.5, 4.5), 33.0)
        self.assertAlmostEqual(lateralsurface_cuboid(0.5, 0.5, 0.5), 4.0)

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
