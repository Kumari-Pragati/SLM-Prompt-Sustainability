import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(5, 10), 157.07963267948966)

    def test_zero_height(self):
        self.assertEqual(volume_cone(5, 0), 0)

    def test_zero_radius(self):
        self.assertEqual(volume_cone(0, 10), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_cone(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            volume_cone(5, -10)

    def test_large_numbers(self):
        self.assertAlmostEqual(volume_cone(10000, 20000), 3141592653.589793)
