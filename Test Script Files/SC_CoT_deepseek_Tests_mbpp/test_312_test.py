import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(5, 10), 157.07963267948966)

    def test_boundary_case(self):
        self.assertAlmostEqual(volume_cone(0, 10), 0)
        self.assertAlmostEqual(volume_cone(5, 0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(volume_cone(1, 1), 0.3183098861837907)
        self.assertAlmostEqual(volume_cone(1, 1000), 3141.592653589793)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_cone("5", 10)
        with self.assertRaises(TypeError):
            volume_cone(5, "10")
        with self.assertRaises(TypeError):
            volume_cone("5", "10")
        with self.assertRaises(ValueError):
            volume_cone(-5, 10)
        with self.assertRaises(ValueError):
            volume_cone(5, -10)
        with self.assertRaises(ValueError):
            volume_cone(-5, -10)
