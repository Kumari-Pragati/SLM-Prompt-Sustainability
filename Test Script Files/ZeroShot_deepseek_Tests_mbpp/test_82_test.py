import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_volume_sphere_positive_radius(self):
        self.assertAlmostEqual(volume_sphere(1), 4.1887902047863905)
        self.assertAlmostEqual(volume_sphere(2), 33.510321638291124)
        self.assertAlmostEqual(volume_sphere(3), 113.09733552923254)

    def test_volume_sphere_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_volume_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(-1)
