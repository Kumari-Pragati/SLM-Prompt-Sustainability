import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_sphere(1), 4.1887902047863905)

    def test_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(-1)

    def test_large_radius(self):
        self.assertAlmostEqual(volume_sphere(1000), 4.1887902047863905e+21)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            volume_sphere('a')
