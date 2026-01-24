import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lateralsurface_cuboid(5, 3, 2), 30)

    def test_edge_case_l_zero(self):
        self.assertEqual(lateralsurface_cuboid(0, 3, 2), 12)

    def test_edge_case_w_zero(self):
        self.assertEqual(lateralsurface_cuboid(5, 0, 2), 12)

    def test_edge_case_h_zero(self):
        self.assertEqual(lateralsurface_cuboid(5, 3, 0), 0)

    def test_edge_case_l_w_h_zero(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)

    def test_edge_case_l_w_h_negative(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(-5, -3, -2)
