import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_sphere(2), (4/3)*(3.141592653589793)*(2**3))

    def test_boundary_case(self):
        self.assertAlmostEqual(volume_sphere(0), (4/3)*(3.141592653589793)*(0**3))

    def test_edge_case(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3)*(3.141592653589793)*(1**3))

    def test_negative_input(self):
        with self.assertRaises(Exception):
            volume_sphere(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(Exception):
            volume_sphere('a')
