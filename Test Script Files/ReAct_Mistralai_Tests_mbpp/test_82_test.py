import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_positive_integer(self):
        """Test volume calculation for positive integers"""
        self.assertAlmostEqual(volume_sphere(3), 268.09488736842107, delta=0.001)

    def test_zero(self):
        """Test volume calculation for zero"""
        self.assertEqual(volume_sphere(0), 0)

    def test_negative_number(self):
        """Test volume calculation for negative numbers"""
        with self.assertRaises(ValueError):
            volume_sphere(-1)

    def test_float_number(self):
        """Test volume calculation for float numbers"""
        self.assertAlmostEqual(volume_sphere(2.5), 250.1991601948452, delta=0.01)

    def test_large_number(self):
        """Test volume calculation for large numbers"""
        self.assertAlmostEqual(volume_sphere(100), 6.283185307179586e+26, delta=1e26)
