import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 56)

    def test_edge_case_zero_dimensions(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)

    def test_edge_case_one_dimension(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 16)

    def test_edge_case_negative_dimensions(self):
        self.assertEqual(lateralsurface_cuboid(-1, -2, -3), -16)

    def test_boundary_case_max_dimensions(self):
        self.assertEqual(lateralsurface_cuboid(10**6, 10**6, 10**6), 2*(10**6)*(2*(10**6)))

    def test_boundary_case_min_dimensions(self):
        self.assertEqual(lateralsurface_cuboid(10**-6, 10**-6, 10**-6), 2*(10**-6)*(2*(10**-6)))
