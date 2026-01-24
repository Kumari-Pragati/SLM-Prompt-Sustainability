import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(volume_sphere(1), 4.1887902047863905)
        self.assertAlmostEqual(volume_sphere(2), 33.510321638291124)

    def test_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(-1)

    def test_large_radius(self):
        self.assertAlmostEqual(volume_sphere(1000), 4.1887902047863905e+21)
