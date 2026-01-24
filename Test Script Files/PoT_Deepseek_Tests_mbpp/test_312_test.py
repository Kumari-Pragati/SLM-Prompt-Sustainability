import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(5, 10), 392.69908169872414)

    def test_edge_case(self):
        self.assertAlmostEqual(volume_cone(0, 10), 0)
        self.assertAlmostEqual(volume_cone(5, 0), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(volume_cone(1, 1000000000), 3.141592653589793)
        self.assertAlmostEqual(volume_cone(1000000000, 1), 3.141592653589793)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_cone("5", 10)
        with self.assertRaises(TypeError):
            volume_cone(5, "10")
        with self.assertRaises(ValueError):
            volume_cone(-5, 10)
        with self.assertRaises(ValueError):
            volume_cone(5, -10)
