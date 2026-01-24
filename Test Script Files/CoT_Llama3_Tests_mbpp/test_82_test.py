import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786208)
        self.assertAlmostEqual(volume_sphere(2), 33.510321638291124)
        self.assertAlmostEqual(volume_sphere(3), 113.09733552923254)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_sphere(0), 0)
        self.assertAlmostEqual(volume_sphere(1e-6), 4.188790204786208e-6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_sphere('a')
        with self.assertRaises(TypeError):
            volume_sphere(None)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(volume_sphere(-1), 0)
        self.assertAlmostEqual(volume_sphere(1e10), 4.188790204786208e12)
