import unittest
from mbpp_312_code import pi
from312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(1, 2), (8/3 * pi))

    def test_edge_case_zero_radius(self):
        self.assertAlmostEqual(volume_cone(0, 1), 0)

    def test_edge_case_zero_height(self):
        self.assertAlmostEqual(volume_cone(1, 0), 0)

    def test_boundary_case_radius_equal_height(self):
        self.assertAlmostEqual(volume_cone(1, 1), (1/3 * pi))
