import unittest
from mbpp_312_code import volume_cone
import math

class TestVolumeCone(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(3, 5), (1.0/3) * math.pi * 3 * 3 * 5)

    def test_boundary_condition(self):
        self.assertAlmostEqual(volume_cone(0, 0), 0)

    def test_edge_condition(self):
        self.assertAlmostEqual(volume_cone(1, 1000), (1.0/3) * math.pi * 1 * 1 * 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_cone("3", 5)
