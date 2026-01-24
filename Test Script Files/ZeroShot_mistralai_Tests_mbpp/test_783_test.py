import unittest
from mbpp_783_code import rgb_to_hsv

class TestRgbToHsv(unittest.TestCase):

    def test_rgb_to_hsv_valid_inputs(self):
        self.assertAlmostEqual(rgb_to_hsv(255, 0, 0), (0, 100.0, 100.0))
        self.assertAlmostEqual(rgb_to_hsv(255, 128, 0), (60.0, 100.0, 100.0))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 0), (90.0, 100.0, 100.0))
        self.assertAlmostEqual(rgb_to_hsv(0, 255, 255), (120.0, 100.0, 100.0))
        self.assertAlmostEqual(rgb_to_hsv(255, 255, 255), (0, 0, 100.0))
        self.assertAlmostEqual(rgb_to_hsv(128, 128, 128), (0, 0, 50.0))

    def test_rgb_to_hsv_invalid_inputs(self):
        with self.assertRaises(ValueError):
            rgb_to_hsv(-1, 0, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(256, 0, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, -1, 0)
        with self.assertRaises(ValueError):
            rgb_to_hsv(0, 0, -1)
