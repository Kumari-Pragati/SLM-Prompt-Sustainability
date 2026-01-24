import unittest
from mbpp_82_code import volume_sphere
import math

class TestVolumeSphere(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_sphere(2), (4/3)*math.pi*2**3)

    def test_boundary_condition(self):
        self.assertAlmostEqual(volume_sphere(0), 0)

    def test_edge_condition(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3)*math.pi)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_sphere('a')
