import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_simple_volume(self):
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786208)

    def test_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_sphere(-1)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            volume_sphere('a')

    def test_large_radius(self):
        self.assertAlmostEqual(volume_sphere(10), 5236.587766040214)

    def test_extremely_large_radius(self):
        self.assertAlmostEqual(volume_sphere(100), 523600.0000000001)
