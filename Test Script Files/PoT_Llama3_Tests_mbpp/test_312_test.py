import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(1, 2), 3.14159265359)

    def test_zero_radius(self):
        self.assertEqual(volume_cone(0, 2), 0)

    def test_zero_height(self):
        self.assertEqual(volume_cone(1, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_cone(-1, 2)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            volume_cone(1, -2)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            volume_cone('a', 2)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            volume_cone(1, 'b')
