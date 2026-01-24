import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_positive_integer(self):
        """Test volume_cube with positive integer"""
        self.assertEqual(volume_cube(3), 27)

    def test_zero(self):
        """Test volume_cube with zero"""
        self.assertEqual(volume_cube(0), 0)

    def test_negative_integer(self):
        """Test volume_cube with negative integer"""
        with self.assertRaises(ValueError):
            volume_cube(-1)

    def test_float(self):
        """Test volume_cube with float"""
        self.assertAlmostEqual(volume_cube(2.5), 15.625, delta=0.01)

    def test_large_integer(self):
        """Test volume_cube with large integer"""
        self.assertEqual(volume_cube(100), 10000000)
