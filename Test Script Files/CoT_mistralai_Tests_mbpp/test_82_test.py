import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786391)
        self.assertAlmostEqual(volume_sphere(2), 33.51928075505862)
        self.assertAlmostEqual(volume_sphere(3), 113.09722553164274)

    def test_zero_value(self):
        self.assertEqual(volume_sphere(0), 0.0)

    def test_negative_value(self):
        self.assertRaises(ValueError, volume_sphere, -1)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, volume_sphere, 'invalid')
