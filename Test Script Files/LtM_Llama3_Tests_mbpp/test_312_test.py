import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):
    def test_volume_cone_typical(self):
        self.assertAlmostEqual(volume_cone(1, 2), 3.14159265359, places=5)

    def test_volume_cone_zero_radius(self):
        self.assertEqual(volume_cone(0, 2), 0)

    def test_volume_cone_zero_height(self):
        self.assertEqual(volume_cone(1, 0), 0)

    def test_volume_cone_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_cone(-1, 2)

    def test_volume_cone_negative_height(self):
        with self.assertRaises(TypeError):
            volume_cone(1, -2)

    def test_volume_cone_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            volume_cone('a', 2)

    def test_volume_cone_non_numeric_height(self):
        with self.assertRaises(TypeError):
            volume_cone(1, 'b')
