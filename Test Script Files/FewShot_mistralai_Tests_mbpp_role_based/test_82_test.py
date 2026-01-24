import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(volume_sphere(3), 28.5413230767447)

    def test_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(-1)

    def test_large_radius(self):
        self.assertAlmostEqual(volume_sphere(1000), 6.28318530717959e+23)
