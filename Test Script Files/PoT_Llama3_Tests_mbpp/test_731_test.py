import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 10), 78.53981633974483)

    def test_edge_case_r_zero(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 10), 0)

    def test_edge_case_h_zero(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 0), 0)

    def test_edge_case_r_and_h_zero(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 0), 0)

    def test_edge_case_r_negative(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone(-5, 10)

    def test_edge_case_h_negative(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone(5, -10)

    def test_edge_case_r_and_h_negative(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone(-5, -10)
