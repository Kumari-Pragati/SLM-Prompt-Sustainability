import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(volume_sphere(3), 268.09488736842008)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(volume_sphere(0), 0)
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786391)
        self.assertAlmostEqual(volume_sphere(22), 33510406.766044474)

    def test_negative_input(self):
        self.assertRaises(ValueError, volume_sphere, -1)

    def test_float_input(self):
        self.assertAlmostEqual(volume_sphere(2.5), 283.1680758807747)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, volume_sphere, 'a')
