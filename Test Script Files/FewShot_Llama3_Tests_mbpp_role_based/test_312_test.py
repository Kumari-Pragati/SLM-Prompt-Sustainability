import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):
    def test_positive_radius_and_height(self):
        self.assertAlmostEqual(volume_cone(2, 3), (1.0/3) * math.pi * 2 * 2 * 3)

    def test_zero_radius(self):
        self.assertEqual(volume_cone(0, 3), 0)

    def test_zero_height(self):
        self.assertEqual(volume_cone(2, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_cone(-2, 3)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            volume_cone(2, -3)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            volume_cone('a', 3)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            volume_cone(2, 'b')
