import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cone(5, 10), 785.3981633974483)

    def test_zero_radius(self):
        with self.assertRaises(ZeroDivisionError):
            volume_cone(0, 10)

    def test_zero_height(self):
        self.assertEqual(volume_cone(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_cone(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            volume_cone(5, -10)

    def test_zero_radius_and_height(self):
        self.assertEqual(volume_cone(0, 0), 0)

    def test_non_integer_radius(self):
        self.assertAlmostEqual(volume_cone(5.5, 10), 785.3981633974483)

    def test_non_integer_height(self):
        self.assertAlmostEqual(volume_cone(5, 10.5), 785.3981633974483)
