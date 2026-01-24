import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(volume_cone(1, 2), 6.283185307179586)
        self.assertAlmostEqual(volume_cone(2, 3), 33.501446248979594)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(volume_cone(0, 1), 0)
        self.assertAlmostEqual(volume_cone(1, 0), 0)
        self.assertAlmostEqual(volume_cone(1, math.nan), math.nan)
        self.assertAlmostEqual(volume_cone(1, math.inf), math.inf)
        self.assertAlmostEqual(volume_cone(math.nan, 1), math.nan)
        self.assertAlmostEqual(volume_cone(math.inf, 1), math.inf)
