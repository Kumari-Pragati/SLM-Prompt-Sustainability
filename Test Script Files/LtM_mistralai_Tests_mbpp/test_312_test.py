import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(volume_cone(1, 2), 6.283185307179586)
        self.assertAlmostEqual(volume_cone(2, 3), 33.51048925178979)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(volume_cone(0, 1), 0)
        self.assertAlmostEqual(volume_cone(1, 0), 0)
        self.assertAlmostEqual(volume_cone(1, math.pi), 4.188790204786391)
        self.assertAlmostEqual(volume_cone(math.pi, 1), 3.141592653589793)

    def test_negative_input(self):
        self.assertAlmostEqual(volume_cone(-1, 2), 0)
        self.assertAlmostEqual(volume_cone(1, -2), 0)

    def test_complex_input(self):
        self.assertAlmostEqual(volume_cone(math.sqrt(2), math.sqrt(3)), 3.464101615139747)
        self.assertAlmostEqual(volume_cone(math.e, math.pi), 11.08349186253968)
